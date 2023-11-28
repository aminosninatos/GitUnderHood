Definitions
---------------
Node or Minion is a machine (Physical or virtual).
Cluster is a set of nodes, each node consist of a Master and workers.
Pod contains in most cases a container.

Commands
----------
> kubectl cluser-info
> kubectl get nodes
> kubectl get all
to get information abou the cluser and its nodes.

Simple kubernetes deployment without yml file
-----------------------------------------------
> kubectl run nginx --image nginx:latest
> kubectl get pods -o wide
> kubectl describe pods

Sample pod definition yaml file
------------------------------------------
apiVersion: v1
kind: Pod
metadata:
        name: myapp-pod
        labels:
                app: myapp
                type: front-end
spec:
        containers:
                - name : nginx-container
                  image: nginx
-------------------------------------------
to run this pod:
> kubectl create -f pod-definition.yml
to delete it:
> kubectl delete pods pod_name

Sample deployment yaml file
-------------------------------------------------
apiVersion: apps/v1
kind: Deployment
metadata:
        name: myapp-rc
        labels:
                app: myapp
                type: front-end
spec:
        template:
                metadata:
                        name: myapp-pod
                        labels:
                                app: myapp
                                type: front-end
                spec:
                        containers:
                                - name : nginx-container
                                  image: nginx
        replicas: 4
        selector:
                matchLabels:
                        type: front-end
--------------------------------------------------------
to run this deployment:
> kubectl create -f deployment-definition.yml
to delete it:
> kubectl delete deployment deployment_name

Sample replicationset yaml file
-----------------------------------------------------------
apiVersion: apps/v1
kind: ReplicaSet
metadata:
        name: myapp-replicaset
        labels:
                app: myapp
                type: front-end
spec:
        template:
                metadata:
                        name: myapp-pod
                        labels:
                                app: myapp
                                type: front-end
                spec:
                        containers:
                                - name : nginx-container
                                  image: nginx
        replicas: 3
        selector:
             matchLabels:
                type: front-end
----------------------------------------------------------------
to run this replicaset:
> kubectl create -f replicaset-definition.yml
to get info about it:
> kubectl get replicaset
to scale it:
> kubectl replace -f replicaset-definition.yaml
> kubectl scale --replicas=6 -f replicaset-definition.yml

Sample namespace yaml file
---------------------------
apiVersion: v1
kind: Namespace
metadata:
        name: dev
----------------------------
to create a namespace:
> kubectl create -f namespace-definition.yaml
or
> kubectl create namespace dev
to get pods for a namespace:
> kubectl get pods --namespace=dev
to view pods in all namespaces
> kubectl get pods --all-namespaces
by default 3 namespaces are created : kube-system, default and kube-public.
to set a default namespace:
> kubectl config set-context $(kubectl config current-context) --namespace=dev

Services types
----------------
NodePort, ClusterIP and Loadbalancer

Sample NodePort service yaml file
---------------------------------------
apiVersion: v1
kind: Service
metadata:
        name: myapp-service
spec:
        type: NodePort
        ports:
                - targetPort: 80
                  port: 80
                  nodePort: 30008
        selector:
                app: myapp
                type: front-end
-----------------------------------------
to run this service:
> kubectl create -f service-definition.yml
to see running services:
> kubectl get services
