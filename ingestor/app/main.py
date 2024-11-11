import http.client as http_client
import logging
import os
import subprocess
import time
from base64 import b64encode
from datetime import datetime
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from ogr2vrt_simple import HttpSource, FileSource
from pydantic import BaseModel

from .airflow_client.airflow_api_stable_client import AuthenticatedClient
from .airflow_client.airflow_api_stable_client.api.dag import get_dags
from .airflow_client.airflow_api_stable_client.api.dag_run import post_dag_run, get_dag_run
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


@app.get("/api/helloworld")
def read_root():
    return {"Hello": "World"}


@app.get("/api/dags")
def read_dags():
    with get_client() as client:
        collection: DAGCollection = get_dags.sync(client=client)
        # map to an array of DAG ids
        dag_ids = [dag.dag_id for dag in collection.dags]
        return {"dags": dag_ids}


@app.get('/api/inspect')
def inspect_datasource(source: str):
    datasource = source
    config = {
        "filename": "",
        "relative_to_file": True,
        "db_friendly": True,
        "no_vsicurl": False,
        "data_formats": "",
    }
    if datasource.startswith("http"):
        vrt_factory = HttpSource(datasource, config)
    else:
        vrt_factory = FileSource(datasource, config)
    vrt_xml = vrt_factory.build_vrt()
    timestamp = datetime.timestamp(datetime.now())
    vrt_path = f"/tmp/{timestamp}.xml"
    if vrt_xml:
        with open(vrt_path, "w") as f:
            f.write(vrt_xml)
    # ogr_info = os.system(f'ogrinfo {vrt_path}')
    ogr_info = subprocess.check_output(["ogrinfo", vrt_path]).decode()
    return f"""
OGR info:
{ogr_info}

VRT file:
{vrt_xml}
"""


class DataSourceBody(BaseModel):
    uri: str
    title: str


@app.post('/api/import')
def import_datasource(body: DataSourceBody):
    dag_id = "ingest_data_postgis"
    with get_client() as client:
        conf = DAGRunConf()
        conf["datasource_uri"] = body.uri
        conf["datasource_title"] = body.title
        dag_run = post_dag_run.sync(client=client, dag_id=dag_id, body=DAGRun(
            conf=conf,
            note="this run was generated automatically by the data ingestor"
        ))
        dag_run_id = dag_run.dag_run_id
        while dag_run.state == "running" or dag_run.state == "queued":
            dag_run = get_dag_run.sync(client=client, dag_id=dag_id, dag_run_id=dag_run_id)
            time.sleep(1)

    return {"result": dag_run.to_dict()}


app.mount("/", StaticFiles(directory="./app/static", html=True), name="static")
