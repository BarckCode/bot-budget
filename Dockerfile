FROM ubuntu:20.10

WORKDIR /opt/libs/apps

COPY requirements.txt .

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip && \
    pip3 install -r requirements.txt && \
    pip3 install pymongo[srv]

WORKDIR /apps

CMD ["tail", "-f", "/dev/null"]