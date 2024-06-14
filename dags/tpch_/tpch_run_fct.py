from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from dbtOp.dbt_operator import DbtOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

_default_args = {
    'max_active_runs': 1,
    'catchup': False,
    'start_date': datetime(year=2020, month=9, day=1)
}

with DAG(
    dag_id = 'run_tpch_fct',
    default_args= _default_args,
    start_date = datetime(2024,6,3,1),
    schedule_interval = None
) as dag:
    

    task1 = DbtOperator(
        task_id='run_dim_order_items',
        dbt_command='dbt run -s dim_order_items.sql'
    )

    task2 = DbtOperator(
        task_id='run_fct_orders',
        dbt_command='dbt run -s fct_orders.sql'
    )

    trigger_stg = TriggerDagRunOperator(
        task_id='trigger_stg_tpch',
        trigger_dag_id='run_tpch', #ID of the dag to trigger,这里是tpch_run_stg里的dag_id
        execution_date='{{ ds }}', #只有2个dag在相同日期的时候才能执行
        reset_dag_run=True, #允许同一个日期多次执行
        wait_for_completion=True, #等待tpch_run_stg里任务完成后，如果不加的话后面的storagin等三个任务会一直执行
        poke_interval= 10  #检测tpch_run_stg是否完成10s一次
    )

trigger_stg >> task1 >> task2 
