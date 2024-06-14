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
    dag_id = 'run_tpch_all',
    default_args= _default_args,
    start_date = datetime(2024,6,3,1),
    schedule_interval = None
) as dag:
    
    task1 = DbtOperator(
        task_id='run_stg_tpch_orders',
        dbt_command='dbt run -s stg_tpch_orders.sql'
    )

    task2 = DbtOperator(
        task_id='run_stg_tpch_lineItems',
        dbt_command='dbt run -s stg_tpch_line_items.sql'
    )
    

    task3 = DbtOperator(
        task_id='run_dim_order_items',
        dbt_command='dbt run -s dim_order_items.sql'
    )

    task4 = DbtOperator(
        task_id='run_fct_orders',
        dbt_command='dbt run -s fct_orders.sql'
    )
 
    task5 = DbtOperator(
        task_id='test_fct',
        dbt_command='dbt test'
    )


[task1,task2] >> task3 >> task4 >> task5