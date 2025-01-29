from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args={
    'owner': "verma",
    'retries': 2,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id="Ex_DAG_1",
    description="this is the dag 1 creation example",
    start_date=datetime(2025,1,28),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    task1=BashOperator(
        task_id='first_dag1_task1',
        bash_command="echo hellow this is my task1 from dag1"
    )
    task1