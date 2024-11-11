import http.client as http_client
import logging
import os
from base64 import b64encode
from fastapi import FastAPI

from .airflow_client.airflow_api_stable_client import AuthenticatedClient
from .airflow_client.airflow_api_stable_client.api.dag import get_dags
from .airflow_client.airflow_api_stable_client.api.dag_run import post_dag_run
from .airflow_client.airflow_api_stable_client.models import DAGCollection, DAGRun, DAGRunConf

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# this will log HTTP requests
http_client.HTTPConnection.debuglevel = 1

airflow_url = os.environ.get("AIRFLOW_URL") or "http://localhost:8080"

app = FastAPI()


def get_client():
    encoded_credentials = b64encode(f"airflow:airflow".encode()).decode()
    client = AuthenticatedClient(base_url=airflow_url + "/api/v1", token=encoded_credentials).with_headers(
        {"Content-Type": "application/json"})
    client.prefix = "Basic"
    return client


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/dags")
def read_dags():
    with get_client() as client:
        collection: DAGCollection = get_dags.sync(client=client)
        # map to an array of DAG ids
        dag_ids = [dag.dag_id for dag in collection.dags]
        return {"dags": dag_ids}


@app.get('/import')
def import_datasource(source: str):
    with get_client() as client:
        conf = DAGRunConf()
        conf["datasource_uri"] = source
        post_dag_run.sync(client=client, dag_id="ingest_data_postgis", body=DAGRun(
            conf=conf,
            note="this run was generated automatically by the data ingestor"
        ))

    return {"status": "success"}
