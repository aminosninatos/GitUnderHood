Introduction
-------------
When using Docker extensively, the management of several different containers quickly becomes cumbersome.
Docker Compose is a tool that helps us overcome this problem and easily handle multiple containers at once.
In short, Docker Compose works by applying many rules declared within a single docker-compose.yml configuration file.
so that in the end, we just need to run:
$ docker-compose up

Docker-compose file
--------------------
In this file, we need to specify the version of the Compose file format, at least ONE SERVICE, and optionally volumes and networks:
version: "3.7"
services:
  ...
volumes:
  ...
networks:
  ...

SERVICES refer to the containers’ configuration:
services:
  frontend:
    image: my-vue-app
    ...
  backend:
    image: my-springboot-app
    ...
  db:
    image: postgres
    ...

VOLUME is a shared directory in the host, visible from some or all containers.
NETWORKS define the communication rules between containers, and between a container and the host.

Pulling an image
-----------------
services: 
  my-service:
    image: ubuntu:latest
    ...

Configuring the Networking
----------------------------
A service can communicate with another service on the SAME NETWORK by simply referencing it by the 
container name and port, provided that we’ve made the port accessible through the expose keyword:
services:
  network-example-service:
    image: karthequian/helloworld:latest
    expose:
      - "80"

To reach a container from the HOST, the ports must be exposed declaratively through the ports keyword:
services:
  network-example-service:
    image: karthequian/helloworld:latest
    ports:
      - "80:80"

we can define additional virtual networks to isolate our containers:      
services:
  network-example-service:
    image: karthequian/helloworld:latest
    networks: 
      - my-shared-network
    ...
  another-service-in-the-same-network:
    image: alpine:latest
    networks: 
      - my-shared-network
    ...
  another-service-in-its-own-network:
    image: alpine:latest
    networks: 
      - my-private-network
    ...
networks:
  my-shared-network: {}
  my-private-network: {}

In this last example, we can see that another-service-in-the-same-network
will be able to ping and reach port 80 of network-example-service, while another-service-in-its-own-network won’t. 

 Setting Up the Volumes
-------------------------
We can configure HOST volumes at the service level, and NAMED volumes in the outer level of the configuration so 
named volumes are visible to all containers.
services:
  volumes-example-service:
    image: alpine:latest
    volumes: 
      - my-named-global-volume:/my-volumes/named-global-volume
      - /tmp:/my-volumes/host-volume
      - /home:/my-volumes/readonly-host-volume:ro
    ...
  another-volumes-example-service:
    image: alpine:latest
    volumes:
      - my-named-global-volume:/another-path/the-same-named-global-volume
    ...
volumes:
  my-named-global-volume: 

Here, both containers will have read/write access to the my-named-global-volume shared folder,
regardless of which path they’ve mapped it to. Instead, the two host volumes will be available 
only to volumes-example-service.

Environment Variables
----------------------
We can define static environment variables, as well as dynamic variables, with the ${} notation:

services:
  database: 
    image: "postgres:${POSTGRES_VERSION}"
    environment:
      DB: mydb
      USER: "${USER}"

To provide those values to Compose.
one method is setting them in a .env file in the same directory, structured like:
POSTGRES_VERSION=alpine
USER=foo

Otherwise, we can set them in the OS before calling the command:
export POSTGRES_VERSION=alpine
export USER=foo
docker-compose up

Finally, we might find it easy to use a simple one-liner in the shell:
POSTGRES_VERSION=alpine USER=foo docker-compose up

