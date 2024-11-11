import logging
import os
from airflow.decorators import task, dag
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
    load_vrt_in_postgis(create_vrt_from_file())


ingest_data_postgis_dag = ingest_data_postgis()
