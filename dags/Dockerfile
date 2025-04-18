FROM apache/airflow:2.5.1-python3.11


# Set environment variables to avoid interactive prompts during install
ENV AIRFLOW_HOME=/opt/airflow

# Set working directory
WORKDIR $AIRFLOW_HOME

# Install basic system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY dags/requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY dags /opt/airflow/dags
COPY dags/train.py /opt/airflow/train.py
