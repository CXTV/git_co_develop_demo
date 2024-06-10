FROM apache/airflow:2.8.4 
COPY requirements.txt requirements.txt
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt
