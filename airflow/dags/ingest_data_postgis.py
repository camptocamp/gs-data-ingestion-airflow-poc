import logging
import os
import requests
from airflow.decorators import task, dag
from airflow.operators.python import get_current_context
from datetime import datetime
from ogr2vrt_simple import HttpSource, FileSource

from airflow import AirflowException

task_logger = logging.getLogger("airflow.task")


@task(
    doc_md="""
This task creates a temporary VRT file out of an external data source.
"""
)
def create_vrt_from_file(params):
    datasource = params["datasource_uri"]
    if (not datasource):
        raise AirflowException('No datasource URI provided')

    task_logger.info(f"Creating VRT from {datasource}")
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
            task_logger.info(f"VRT file written to {vrt_path}")
    else:
        raise AirflowException('VRT could not be generated')

    return vrt_path


@task(
    doc_md="""
This task will load the data that a VRT file points to into a PostgreSQL/PostGIS database
"""
)
def load_vrt_in_postgis(vrt_path):
    task_logger.info(f"Loading VRT into PostGIS: {vrt_path}")
    # convert VRT to PostGIS
    os.system(
        f'ogr2ogr -f PostgreSQL PG:"dbname=postgis host=postgis port=5433 user=postgis password=postgis active_schema=public" {vrt_path}')
    task_logger.info("Data successfully loaded into PostGIS")


@task(
    doc_md="""
This task will create a metadata in GeoNetwork for the ingested dataset
"""
)
def create_metadata():
    title = get_current_context()["ti"]["datasource_title"]
    task_logger.info(f"Creating metadata with title: {title}")

    record_xml = f"""
<simpledc xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dct="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://localhost:8080/geonetwork/xml/schemas/dublin-core/schema.xsd">
    <dc:title>{title}</dc:title>
    <dc:creator/>
    <dc:subject/>
    <dc:subject/>
    <dc:description/>
    <dc:publisher/>
    <dc:type/>
    <dc:format>text/plain</dc:format>
    <dc:language>eng</dc:language>
    <dc:coverage>North 90, South -90, East -180, West 180. Global</dc:coverage>
    <dc:rights/>
    <dct:created/>
    <dct:dateSubmitted/>
    <dct:modified>2024-11-11T19:48:28.998379Z</dct:modified>
    <dc:identifier>_empty_</dc:identifier>
</simpledc>
"""
    response = requests.post("http://geonetwork:8080/api/records?metadataType=METADATA&uuidProcessing=GENERATEUUID",
                             data=record_xml,
                             headers={"Content-Type": "application/xml"},
                             )
    task_logger.info(response)

    task_logger.info("Data successfully loaded into PostGIS")


@dag(
    schedule=None,
    catchup=False,
    params={
        "datasource_uri": "",
        "datasource_title": "Unknown title"
    },
    doc_md="""
Loads a dataset described by the `datasource_uri` parameter into a PostgreSQL database
"""
)
def ingest_data_postgis():
    # extractTask = create_vrt_from_file()
    # loadTask = load_vrt_in_postgis()
    load_vrt_in_postgis(create_vrt_from_file()) >> create_metadata()


ingest_data_postgis_dag = ingest_data_postgis()
