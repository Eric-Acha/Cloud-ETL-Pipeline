from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Add project root to path so Airflow can find the ETL modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.extract import extract
from etl.transform import transform
from etl.load import load
from etl.logger import get_logger

logger = get_logger()

# Default DAG arguments
default_args = {
    'owner': 'eric_acha',       
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_etl():
    logger.info("Starting Airflow ETL pipeline")

    df = extract()
    logger.info(f"Extraction complete")

    df = transform(df)
    logger.info(f"Transformation complete")

    load(df)
    logger.info(f"Loading complete")

    logger.info("Airflow ETL pipeline finished successfully")

with DAG(
    dag_id="api_etl_pipeline",
    default_args=default_args,
    description="Fake store API ETL pipeline",
    schedule_interval="@daily",
    start_date=datetime(2026, 3, 3),
    catchup=False,
    tags=["etl", "api", "postgres"],
) as dag:
    
    etl_task = PythonOperator(
        task_id="run _fake_store_etl",
        python_callable=run_etl,
    )

    etl_task


   