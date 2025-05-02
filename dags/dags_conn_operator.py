from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_conn_operator",
    schedule=None,
    start_date=pendulum.datetime(2025, 5, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    t1 = BashOperator(
        task_id="t1",
        bash_command="t1"
    )
     
    t2 = BashOperator(
        task_id="t2",
        bash_command="t2"
    )

    t3 = BashOperator(
        task_id="t3",
        bash_command="t3"
    )    

    t4 = BashOperator(
        task_id="t4",
        bash_command="t4"
    )

    t5 = BashOperator(
        task_id="t5",
        bash_command="t5"
    )

    t6 = BashOperator(
        task_id="t6",
        bash_command="t6"
    )

    t7 = BashOperator(
        task_id="t7",
        bash_command="t7"
    )

    t8 = BashOperator(
        task_id="t8",
        bash_command="t8"
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8