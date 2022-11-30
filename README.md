# udaconnect-kafka

## Environment set-up

For this project you need to...

- Install Docker
- Set up a DockerHub account
- Set up kubectl
- Install VirtualBox with at least version 6.0
- Install Vagrant with at least version 2.0

[MISSING]

## How to set up Kafka in Kubernetes

1. Installation
$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh

2. Run Kafka with helm
$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm install kafka-release bitnami/kafka

If error "Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version?timeout=32s": dial tcp 127.0.0.1:8080: 
connect: connection refused" occurs:

export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
kubectl config view --raw > ~/.kube/config


## Test if it works
Verifying it Works

The following pages should be accessible by web browser:

    http://localhost:30000/ - Frontend
    http://localhost:30003/ - Persons API
    http://localhost:30002/ - Connection API
    http://localhost:30005/ - Location API
    

[MISSING]
