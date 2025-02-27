from airflow import DAG
from airflow.providers.google.cloud.operators.dataflow import DataflowCreateJobOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2025, 2, 27),
    "retries": 1
}

with DAG(
    "dataflow_private_network",
    schedule_interval="0 8 * * *",  # Runs daily at 8 AM IST
    default_args=default_args,
    catchup=False
) as dag:

    dataflow_job = DataflowCreateJobOperator(
        task_id="run_dataflow_job",
        job_name="my-dataflow-private-network",
        template="gs://your-bucket/template-path",
        location="us-central1",
        parameters={
            "url": "https://atexturl.",
            "network": "default",
            "subnetwork": "regions/us-central1/subnetworks/my-subnet",
            "ipConfiguration": "WORKER_IP_PRIVATE"
        },
        environment={
            "network": "default",
            "subnetwork": "regions/us-central1/subnetworks/my-subnet",
            "ipConfiguration": "WORKER_IP_PRIVATE"
        }
    )
