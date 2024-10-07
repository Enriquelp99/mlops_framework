FROM ubuntu:24.04

# Install necessary tools (curl, git, tar, gzip)
RUN apt-get update && \
    apt-get install -y git curl tar gzip python3 python3-pip python3-venv && \
    apt-get clean

# Install OpenJDK 11
RUN apt-get install -y openjdk-11-jdk && \
    apt-get clean

# Install Scala downloading it directly from the official site
RUN curl -O https://downloads.lightbend.com/scala/2.13.12/scala-2.13.12.tgz && \
    tar -xvf scala-2.13.12.tgz && \
    mv scala-2.13.12 /opt/scala && \
    rm scala-2.13.12.tgz

# Assign correct permissions to Scala
RUN chmod -R 755 /opt/scala

# Configure environment variables for Scala and Java
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV SCALA_HOME=/opt/scala
ENV SPARK_HOME=/opt/spark
ENV PATH=$JAVA_HOME/bin:$SCALA_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH

RUN python3 -m venv /opt/venv

# Download and install Spark 3.5.3 with Hadoop 3
RUN curl -O https://dlcdn.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz && \
    tar -xvf spark-3.5.3-bin-hadoop3.tgz && \
    mv spark-3.5.3-bin-hadoop3 /opt/spark && \
    rm spark-3.5.3-bin-hadoop3.tgz && \
    # Verify installation
    ls -la /opt/spark/sbin/ && \
    ls -la /opt/spark/

# Assign correct permissions to Spark
RUN chmod -R 755 /opt/spark

# Copy project code
COPY ../src /tmp/src
COPY ../worker.py /tmp/worker.py

# Install dependencies in requirements.txt
RUN /opt/venv/bin/pip install --no-cache-dir -r /tmp/src/requirements.txt
ENV PATH=/opt/venv/bin:$PATH

# Set the working directory
WORKDIR /tmp/