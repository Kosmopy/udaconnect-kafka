FROM python:3.9.7

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5006

WORKDIR .
COPY kafka-consumer.py kafka-consumer.py
ENTRYPOINT ["python", "kafka-consumer.py"]
