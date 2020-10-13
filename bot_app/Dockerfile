FROM ubuntu:20.10
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip && \
    pip3 install python-telegram-bot && \
    pip3 install pymongo && \
    pip3 install pymongo[srv]
WORKDIR /apps
CMD ["tail", "-f", "/dev/null"]