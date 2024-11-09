FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt update && apt install -y gdal-bin libgdal-dev build-essential
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 80

CMD ["fastapi", "dev", "app/main.py", "--port", "80", "--host", "0.0.0.0"]
