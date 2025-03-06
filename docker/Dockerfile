FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y git curl tar gzip python3 python3-pip python3-venv && \
    apt-get clean

RUN apt-get install -y openjdk-11-jdk && \
    apt-get clean

RUN curl -O https://downloads.lightbend.com/scala/2.13.12/scala-2.13.12.tgz && \
    tar -xvf scala-2.13.12.tgz && \
    mv scala-2.13.12 /opt/scala && \
    rm scala-2.13.12.tgz

RUN chmod -R 755 /opt/scala

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SCALA_HOME=/opt/scala
ENV SPARK_HOME=/opt/spark
ENV PATH=$JAVA_HOME/bin:$SCALA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

RUN python3 -m venv /opt/venv

RUN curl -O https://apache.root.lu/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz && \
    tar -xvf spark-3.4.1-bin-hadoop3.tgz && \
    mv spark-3.4.1-bin-hadoop3 /opt/spark && \
    rm spark-3.4.1-bin-hadoop3.tgz && \

    ls -la /opt/spark/sbin/ && \
    ls -la /opt/spark/

RUN chmod -R 755 /opt/spark

RUN apt-get update && apt-get install -y netcat-openbsd

COPY ../src /tmp/src
COPY ../worker.py /tmp/worker.py

RUN /opt/venv/bin/pip install --no-cache-dir -r /tmp/src/requirements.txt
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /tmp/