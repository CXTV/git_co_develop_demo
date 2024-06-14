from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from dbtOp.dbt_operator import DbtOperator

_default_args = {
    'max_active_runs': 1,
    'catchup': False,
    'start_date': datetime(year=2020, month=9, day=1)
}

with DAG(
    dag_id = 'debug_dbt',
    default_args= _default_args,
    start_date = datetime(2024,2,3,1),
    schedule_interval = None
) as dag:
    task1 = DbtOperator(
        task_id='debug_dbt_task',
        dbt_command='debug'
    )
    
task1