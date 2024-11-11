ARG AIRFLOW_IMAGE_NAME

FROM ${AIRFLOW_IMAGE_NAME:-apache/airflow:2.10.3}

USER root
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    gdal-bin libgdal-dev build-essential \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir "GDAL==3.6.2" ogr2vrt_simple
