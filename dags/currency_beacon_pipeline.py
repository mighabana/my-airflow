import os
from datetime import timedelta

from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow.models import DAG
from airflow.sdk import timezone

default_args = {
    "owner": "mhabana",
    "email": "mighabana@gmail.com",
    "start_date": timezone.datetime(2026,2,9),
    "retries": 3,
    "retry_exponential_backoff": False,
    "max_retry_delay": timedelta(minutes=10),
    "email_on_retry": False,
}

dag = DAG(
    dag_id="currency_beacon_pipeline",
    default_args=default_args,
    schedule= "0 */1 * * *",
    catchup=False,
    max_active_runs=1
)

base_currencies = ["USD", "PHP", "EUR"]

latest_currencies = KubernetesPodOperator(
    task_id=f"{dag.dag_id}_latest_currencies",
    name="currency-beacon-latest",
    namespace="airflow",
    image="mighabana/infolio:latest",
    cmds=["python"],
    arguments=["pipelines/currency_beacon_to_s3.py", "current", "--base_currencies", *base_currencies, "--bucket_name", "currency-beacon", "--path_prefix", "/exchange_rates"],
    env_vars={
        "API__CURRENCY_BEACON__API_KEY": os.environ.get("CURRENCY_BEACON_API_KEY"),
        "CONNECTOR__S3__ENDPOINT_URL": os.environ.get("S3_ENDPOINT_URL"),
        "CONNECTOR__S3__ACCESS_KEY_ID": os.environ.get("S3_ACCESS_KEY_ID"),
        "CONNECTOR__S3__SECRET_ACCESS_KEY": os.environ.get("S3_SECRET_ACCESS_KEY")
    },
    get_logs=True,
    image_pull_policy='Always',
    dag=dag
)
