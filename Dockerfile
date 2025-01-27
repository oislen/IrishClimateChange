# get base image
FROM ubuntu:latest

# set environment variables
ENV user=ubuntu
ENV DEBIAN_FRONTEND=noninteractive
# set python version
ARG PYTHON_VERSION="3.12"
ENV PYTHON_VERSION=${PYTHON_VERSION}

# install required software and programmes for development environment
RUN apt-get update 
RUN apt-get install -y apt-utils vim curl wget unzip tree htop

# set up home environment
RUN mkdir -p /home/${user} && chown -R ${user}: /home/${user}

# clone git repo
COPY . /home/ubuntu/IrishClimateDashboard

# add deadsnakes ppa
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
# install required python and create virtual environment
RUN apt-get install -y python${PYTHON_VERSION} python${PYTHON_VERSION}-venv 
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN /opt/venv/bin/python3 -m pip install -v -r /home/ubuntu/IrishClimateDashboard/requirements.txt

WORKDIR /home/${user}/IrishClimateDashboard
CMD ["bokeh", "serve","dashboard/bokeh_dash_app.py"]