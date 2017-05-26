# coding: utf-8

# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators import PythonOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2017, 5, 11),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    # 'retries': 2,
    # 'retry_delay': timedelta(minutes=2),
    'provide_context': False
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'schedule_interval': '20 16 * * *',
    # 'end_date': datetime(2016, 1, 1),
}

test_dag = DAG('test_airflow', default_args=default_args,
               schedule_interval="*/2 * * * *")


def test():
    print("get data")


pv_raw = PythonOperator(
    task_id='pv_raw',
    python_callable=test,
    dag=test_dag)
