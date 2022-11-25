FROM python:3.9.7

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5004

WORKDIR .
COPY . /
COPY main.py main.py
ENTRYPOINT ["python", "main.py"]