# data-ingestor

This is the data-ingestor package.

Based on the [Python Project Bootstrap](https://github.com/tomkralidis/python-project-bootstrap) template by Tom Kralidis.

### Requirements
- Python 3
- [virtualenv](https://virtualenv.pypa.io)


## Virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To deactivate:
```bash
deactivate
```

## Installing dependencies

```bash
pip install -r requirements.txt
```

## Running

```bash
fastapi dev app/main.py
```

## Using the API

```python
# Python API examples go here
```

## Code Conventions

* [PEP8](https://www.python.org/dev/peps/pep-0008)

```bash
pip install flake8
flake8 main.py
```

## Airflow OpenAPI python client

The data ingestor uses an auto-generated Airflow python client:

```bash
pip install openapi-python-client
openapi-python-client generate --path ../airflow/api.yaml --output-path ./app/airflow_client
```
