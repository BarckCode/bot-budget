FROM ubuntu:20.10

WORKDIR /app

# Copy the application
COPY . .

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip

# Install Libs
RUN pip install -r requirements.txt
RUN pip install \
    pymongo[srv]

# Run app
CMD ["python3", "main.py"]
