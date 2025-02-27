from googleapiclient.discovery import build
import functions_framework

@functions_framework.http
def trigger_dataflow(request):
    dataflow = build('dataflow', 'v1b3')
    project_id = "your-project-id"
    location = "us-central1"

    job = {
        "jobName": "my-dataflow-private-network",
        "parameters": {
            "url": "https://atexturl.",
            "network": "default",
            "subnetwork": "regions/us-central1/subnetworks/my-subnet",
            "ipConfiguration": "WORKER_IP_PRIVATE"
        },
        "environment": {
            "network": "default",
            "subnetwork": "regions/us-central1/subnetworks/my-subnet",
            "ipConfiguration": "WORKER_IP_PRIVATE"
        }
    }

    request = dataflow.projects().locations().templates().launch(
        projectId=project_id, location=location, body=job,
        gcsPath="gs://your-bucket/template-path"
    )
    response = request.execute()
    return response
