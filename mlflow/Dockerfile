FROM python:3.9

COPY mlflow/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

CMD ["mlflow", "server", "--backend-store-uri", "postgresql://user:password@postgres:5432/mlflowdb", "--default-artifact-root", "s3://bucket", "--host", "0.0.0.0", "--port", "8000"]