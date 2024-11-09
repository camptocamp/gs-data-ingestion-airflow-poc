import http.client as http_client
import logging
import os
from base64 import b64encode
from fastapi import FastAPI
from ogr2vrt_simple import HttpSource, FileSource

from .airflow_client.airflow_api_stable_client import AuthenticatedClient
from .airflow_client.airflow_api_stable_client.api.dag import get_dags
from .airflow_client.airflow_api_stable_client.models import DAGCollection

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


@app.get('/vrt')
def generate_vrt(source: str):
    config = {
        "filename": "",
        "relative_to_file": True,
        "db_friendly": True,
        "no_vsicurl": False,
        "data_formats": "",
        "template": "templates/vrt.j2",
    }
    data_source = source
    vrt_factory = None
    if source.startswith("http"):
        vrt_factory = HttpSource(data_source, config)
    else:
        vrt_factory = FileSource(data_source, config)
    vrt_xml = vrt_factory.build_vrt()
    if vrt_xml:
        with open("/tmp/current.vrt", "w") as f:
            f.write(vrt_xml)
            logger.info(f"VRT file written to /tmp/current.vrt")
    else:
        logger.error("error build VRT file")
        return "error"

    # convert VRT to PostGIS
    os.system(
        'ogr2ogr -f PostgreSQL PG:"dbname=postgis host=postgis port=5433 user=postgis password=postgis active_schema=public" /tmp/current.vrt')

    logger.info("Data successfully loaded into PostGIS:")
    logger.info(vrt_xml)

    return {"status": "success"}
