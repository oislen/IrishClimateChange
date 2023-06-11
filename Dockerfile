# get base image
FROM ubuntu:20.04

# set environment variables
ENV user=ubuntu
ENV DEBIAN_FRONTEND=noninteractive

# install required software and programmes for development environment
RUN apt-get update 
RUN apt-get install -y apt-utils vim curl wget unzip git python3 python3-pip tree htop

# install required python packages
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# set up home environment
RUN useradd ${user}
RUN mkdir -p /home/${user} && chown -R ${user}: /home/${user}

# clone git repo
RUN git clone https://github.com/oislen/IrishClimateApp.git /home/ubuntu/IrishClimateApp

WORKDIR /home/${user}/IrishClimateApp/scripts
CMD ["bokeh", "serve","bokeh_line_app.py","bokeh_map_app.py"]