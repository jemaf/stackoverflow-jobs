FROM python:3.6-slim

ENV GIT_DISCOVERY_ACROSS_FILESYSTEM=1
RUN apt-get -o Acquire::Check-Valid-Until=false update \
    && apt-get install -y git

RUN mkdir /workspace
WORKDIR /workspace
ADD requirements.txt /workspace/requirements.txt
RUN pip install -r /workspace/requirements.txt
