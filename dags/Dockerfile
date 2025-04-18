
FROM python:3.11-slim



# Set working directory
WORKDIR /opt/airflow

# Install dependencies
COPY dags/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy DAGs and training script
COPY dags/train.py /opt/airflow/train.py
COPY dags /opt/airflow/dags

