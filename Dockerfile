FROM python:3.9-slim
RUN mkdir /payment
COPY requirements.txt /payment
RUN pip3 install -r /payment/requirements.txt --no-cache-dir
COPY . /payment
WORKDIR /payment