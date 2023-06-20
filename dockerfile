FROM python:3.9.17-slim-bullseye

RUN apt-get update && apt-get install -y \
    apt-utils \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get -y update; 

# Install bids-validator
# RUN apt-get -y install curl
# RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs && apt-get install -y npm
# RUN npm install -g bids-validator@1.5.4

# Copy your application code
WORKDIR /app
COPY . /app
RUN pip install -e .

# Set the entrypoint command
ENTRYPOINT ["pycrostates_cluster"]