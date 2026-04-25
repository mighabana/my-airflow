import os
from datetime import timedelta, UTC

from airflow.operators.python import PythonOperator
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow.timetables.interval import CronDataIntervalTimetable
from airflow.models import DAG
from airflow.sdk import timezone
import pendulum

from utils.stock_tickers import get_batches

default_args = {
    "owner": "mighabana",
    "email": "mighabana@gmail.com",
    "start_date": timezone.datetime(2026, 2, 9),
    "retries": 3,
    "retry_exponential_backoff": False,
    "max_retry_delay": timedelta(minutes=10),
    "email_on_retry": False,
    "email_on_failure": False,
}

dag = DAG(
    dag_id="yahoo_finance_pipeline",
    default_args=default_args,
    schedule=CronDataIntervalTimetable(
        cron="*/15 9-16 * * 1-5",
        timezone=pendulum.timezone("America/New_York")
    ),
    catchup=False,
    max_active_runs=1
)

BATCH_SIZE = 100
batches = get_batches(BATCH_SIZE)
batch_task_ids = []

for i, batch in enumerate(batches):
    task_id = f"{dag.dag_id}_latest_stock_{i}"
    batch_task_ids.append(task_id)

    latest_stock_info = KubernetesPodOperator(
        task_id=task_id,
        name="currency-beacon-latest",
        namespace="airflow",
        image="mighabana/infolio:latest",
        cmds=["python"],
        arguments=["pipelines/yahoo_finance_to_s3.py", "latest", "--tickers", *batch, "--bucket_name", "yahoo-finance", "--path_prefix", "", "--batch_postfix", f"{i}"],
        env_vars={
            "CONNECTOR__S3__ENDPOINT_URL": os.environ.get("S3_ENDPOINT_URL"),
            "CONNECTOR__S3__ACCESS_KEY_ID": os.environ.get("S3_ACCESS_KEY_ID"),
            "CONNECTOR__S3__SECRET_ACCESS_KEY": os.environ.get("S3_SECRET_ACCESS_KEY")
        },
        get_logs=True,
        image_pull_policy='Always',
        do_xcom_push=True,
        pool="yahoo-finance",
        dag=dag
    )

def consolidate_failures(batch_task_ids: list[str], **context) -> None:
    ti = context["ti"]

    all_failed = []
    batch_breakdown = []
    total_requested = 0

    for task_id in batch_task_ids:
        xcom_value = ti.xcom_pull(task_ids=task_id)

        if xcom_value is None:
            batch_breakdown.append({
                "batch": task_id,
                "note": "pod exited before writing XCom - check task logs",
            })
            continue

        failed = xcom_value.get("failed", [])
        requested = xcom_value.get("requested", [])
        total_requested += len(requested)

        if failed:
            all_failed.extend(failed)
            batch_breakdown.append({
                "batch": xcom_value.get("batch", task_id),
                "failed": failed,
                "count": len(failed),
            })

    all_failed_unique = sorted(set(all_failed))
    total_failed = len(all_failed_unique)
    total_batches = len(batch_task_ids)

    if total_failed == 0:
        print(f"✅ All {total_requested} tickers across {total_batches} batches returned data.")
        return

    breakdown_str = "\n".join(
        f"  batch {b['batch']}: {b.get('failed', [])}" for b in batch_breakdown
    )
    raise RuntimeError(
        f"\n❌ {total_failed}/{total_requested} tickers returned no data "
        f"across {total_batches} batches.\n\n"
        f"Failed tickers:\n  {all_failed_unique}\n\n"
        f"Batch breakdown:\n{breakdown_str}"
    )


consolidate_task = PythonOperator(
    task_id="consolidate_failures",
    python_callable=consolidate_failures,
    op_kwargs={"batch_task_ids": batch_task_ids},
    trigger_rule="all_done",
    retries=0,
    dag=dag,
)

for task_id in batch_task_ids:
    dag.get_task(task_id) >> consolidate_task
