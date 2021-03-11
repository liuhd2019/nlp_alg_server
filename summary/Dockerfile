FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y sudo \
    build-essential \
    curl \
    libcurl4-openssl-dev \
    libssl-dev \
    wget \
    python3-dev \
    python3-pip \
    libxrender-dev \
    libxext6 \
    libsm6 \
    openssl \
	vim \
	ctags

RUN mkdir -p /app
COPY requirements-service.txt /app
COPY summarizer /app/summarizer
COPY server.py /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements-service.txt

#ENTRYPOINT ["python3", "./server.py"]
