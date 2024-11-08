# Data ingestion prototype using Airflow

This project is an experiment to demonstrate the feasibility of doing data ingestion from various sources using Apache Airflow.

## Run with docker

First initialize the Airflow database:

```bash
docker compose up airflow-init
```

Then run all services
```bash
docker compose up -d
```

Data ingestor API is on http://localhost:8000.

Airflow UI is on http://localhost:8080.
The default account is `airflow` / `airflow`
