FROM python:3.9.7-slim-buster

RUN apt-get update \
  && apt-get install git -y
RUN pip install git+https://github.com/shenxn/libdyson.git@main \
  && pip install influxdb

ADD ./dyson-graph/* .
CMD ["python", "__init__.py"]
