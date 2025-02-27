FROM apache/airflow:2.10.4-python3.12
COPY /dags ./dags
COPY requirements.txt /requirements.txt
RUN pip install - user - upgrade pip
RUN pip install -r /requirements.txt