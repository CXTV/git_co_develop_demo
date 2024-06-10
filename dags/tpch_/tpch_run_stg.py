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
    dag_id = 'run_stagings',
    default_args= _default_args,
    start_date = datetime(2024,2,3,1),
    schedule_interval = None
) as dag:
    task1 = DbtOperator(
        task_id='run_tpch_orders',
        dbt_command='run -s stg_tpch_orders.sql'
    )
    
task1