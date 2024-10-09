:: set docker settings
SET DOCKER_USER=oislen
SET DOCKER_REPO=irishclimatedashboard
SET DOCKER_TAG=latest
SET DOCKER_IMAGE=%DOCKER_USER%/%DOCKER_REPO%:%DOCKER_TAG%
SET DOCKER_CONTAINER_NAME=icd

:: remove existing docker containers and images
docker image rm -f %DOCKER_IMAGE%

:: build docker image
call docker build --no-cache -t %DOCKER_IMAGE% . 
::call docker build -t %DOCKER_IMAGE% .

:: run docker container
SET UBUNTU_DIR=/home/ubuntu
call docker run --name %DOCKER_CONTAINER_NAME% --shm-size=512m -p 5006:5006 -it %DOCKER_IMAGE%

:: useful docker commands
:: docker images
:: docker ps -a
:: docker exec -it {container_hash} /bin/bash
:: docker stop {container_hash}
:: docker start -ai {container_hash}
:: docker rm {container_hash}
:: docker image rm {docker_image}
:: docker push {docker_image}