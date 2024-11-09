import urllib.request
from airflow.decorators import task, dag


@task
def download_file(uri, target_path):
    with urllib.request.urlopen(uri) as file:
        with open(target_path, "wt") as new_file:
            new_file.write(file.read())


@task
def transform_geojson(geojson_path):
    with open(geojson_path, "rt") as geojson_file:
        # do some transformation
        pass


@dag(schedule=None, catchup=False)
def import_geojson_from_url():
    extractTask = download_file("https://france-geojson.gregoiredavid.fr/repo/regions.geojson", "/tmp/geojson")
    transformTask = transform_geojson("/tmp/geojson")

    extractTask >> transformTask


import_geojson_from_url_dag = import_geojson_from_url()
