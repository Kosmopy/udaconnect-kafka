FROM python:3.9-alpine

WORKDIR .
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN apk add linux-headers
RUN pip install Pillow
RUN pip install grpcio

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5004

WORKDIR .
COPY . /
COPY main.py main.py
ENTRYPOINT ["python", "main.py"]