FROM python:3.7.3-slim
COPY requirements.txt /
RUN pip3 install --upgrade pip setuptools
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
RUN python migrate.py