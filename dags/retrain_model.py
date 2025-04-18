# Airflow DAG for Retraining Model
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dags.train import train  # Import your training function
from airflow import DAG
from airflow.operators.python import PythonOperator
from dags.train import train


from datetime import timedelta


import sys
sys.path.append('/opt/airflow/ml')

# Define your DAG
dag = DAG(
    'train_model_dag',
    description='A simple training model DAG',
    schedule_interval='@daily',  # Or your desired interval
    start_date=datetime(2025, 4, 18),
    catchup=False,
)

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='daily_model_retrain',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
) as dag:

    retrain_task = PythonOperator(
        task_id='retrain_model',
        python_callable=train,
    )
