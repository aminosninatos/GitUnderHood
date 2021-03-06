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
will RUN additionnal commands to an EXISTING container

#docker container inspect --format '{{  .NetworkSettings.IPAddress }}' container_name
will show the ip address of the container

#docker network ls
will show all the virtual Networks

#docker network inspect network_name
will inspect a network

#docker network create --driver driver_name network_name
will create a network

#docker network connect network_name container_name
will attach a container to a network

#docker network disconnect network_name container_name
will disconnect a container from  a

#docker container run --rm image
once its done running, erase everything related to it and save the disk space

#docker history image
will show how image is made of which means different layers of the image.

#docker image inspect image_name
will show the metadaata of an image.

#docker image build -t image_name .
will build an image provided the Dockerfile is in the current directory

#docker volume ls 
will show the list of volumes.

#docker volume inspect volume_name
will inspect a specific volume.

#docker container run --name image_name -v volume_name:directory image
will created a named volume for the image.

#docker container run --name image_name -v directory_host:directory_container image
will map a directory in the host in a directory in the container

#docker swarm init
will initialize swarm and created tokens and certificates

#docker node ls 
will show the list of nodes.

#docker service create 
replace docker run command in swarm world.

#docker service ls 
will show the list of services.

#docker update 
will update the config of one or more containers(CPU, RAM ... )

#docker service update service_id options 
will update the config of a service in swarm.

#docker swarm join --tocken xxxxxxxxxxxxxxx 
to add a worker to the swarm initiated.

#docker node update --role manager node2
to promote node2 from a worker to be a manager

#docker node ps node2
to show containers running in node2

#docker service create --replicas 3 alpine ping 8.8.8.8 
will create 3 replicas of alpine each in every nodes that you have.








