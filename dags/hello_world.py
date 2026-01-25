"""
Example DAG - Hello World

A simple example DAG to verify your Airflow installation is working.
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


def print_context(**context):
    """Print the Airflow context for debugging."""
    print("=" * 50)
    print("Hello from Airflow on K3s!")
    print("=" * 50)
    print(f"Execution date: {context['ds']}")
    print(f"Task instance: {context['task_instance']}")
    print(f"DAG: {context['dag'].dag_id}")
    return "Success!"


def process_data():
    """Example data processing function."""
    import json
    
    data = {
        "status": "processed",
        "timestamp": datetime.now().isoformat(),
        "message": "Data pipeline working correctly",
    }
    print(json.dumps(data, indent=2))
    return data


with DAG(
    dag_id="hello_world",
    default_args=default_args,
    description="A simple hello world DAG to verify installation",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["example", "hello-world"],
) as dag:

    # Task 1: Print hello with Python
    hello_python = PythonOperator(
        task_id="hello_python",
        python_callable=print_context,
    )

    # Task 2: Print system info with Bash
    system_info = BashOperator(
        task_id="system_info",
        bash_command="""
            echo "System Information"
            echo "=================="
            echo "Hostname: $(hostname)"
            echo "Date: $(date)"
            echo "Kernel: $(uname -r)"
            echo "Python: $(python --version 2>&1)"
            echo "Airflow: $(airflow version)"
        """,
    )

    # Task 3: Process some data
    process = PythonOperator(
        task_id="process_data",
        python_callable=process_data,
    )

    # Task 4: Final task
    complete = BashOperator(
        task_id="complete",
        bash_command='echo "Pipeline completed successfully at $(date)"',
    )

    # Define task dependencies
    hello_python >> system_info >> process >> complete
