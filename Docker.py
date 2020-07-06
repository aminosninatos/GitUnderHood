Dokcer
--------

#docker command options (old way)
#docker management-command command options (new way)
docker command line structure

#docker version
to get docker client and server(engine) version

#docker info
get more system info about docker

#docker
to get docker commands

#docker container run --publish 8080:80 --detach --name ohyeah nginx
will download the image nginx and run an instance (container)
--publish will map local port 8080 to container port 80
--detach will run the container in background
--name will name our container

#docker container ls
lists all runnning the containers

#docker container ls -a
lists all the containers stopped and running

#docker container logs name_of_container
will show the logs of the container name

#docker container top name_of_container
will show the process running inside the container

#docker container stop container_id
will stop the container

#docker container top container_id
will show process list in the container

#docker container stats container_id
will show performance stats of the container

#docker container inspect container_id
will show details of the container config

#docker container run -it imgae
will start a NEW container interactively(t:tty i:interactive)

#docker container exec -it container_id
will start a RUN additionnal commands to an EXISTING container
