FROM python:3.10-slim-buster

RUN apt-get update \
  && apt-get install git -y
RUN pip install git+https://github.com/shenxn/libdyson.git@main \
  && pip install influxdb prometheus_client
# TODO: Fix this to use requirements.txt

ADD ./dyson-graph/* .
CMD ["python", "__init__.py", "--influxdb"]
