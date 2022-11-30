# udaconnect-kafka

## 1. Environment set-up

For this project you need to...

- Install Docker
- Set up a DockerHub account
- Set up kubectl
- Install VirtualBox with at least version 6.0
- Install Vagrant with at least version 2.0

## 2. Initialize K3s

To use vagrant with VirtualBox, run the command "vagrant up" in the folder where the Vagrantfile is saved.
 
 vagrant ssh //SSH into the Vgrant environment
 sudo su // get access

## 3. Configure kubectl

Configure your kubetcl ~/.kube/config with the info from the K3s that you can access with:
sudo cat /etc/rancher/k3s/k3s.yaml

## 4. Set up Kafka in Kubernetes

A. Installation
$ curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
$ chmod 700 get_helm.sh
$ ./get_helm.sh

B. Run Kafka with helm
$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm install kafka-release bitnami/kafka

If error "Error: Kubernetes cluster unreachable: Get "http://localhost:8080/version?timeout=32s": dial tcp 127.0.0.1:8080: 
connect: connection refused" occurs:

export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
kubectl config view --raw > ~/.kube/config

## 5. Deploy applications

Run kubectl apply -f deployment/

You can see active pods: kubectl get pods
active services: kubectl get services

If errors occur, you can look into the logs of an pod: kubectl logs <POD_NAME>

## 6. Seed the database

Seed db with following command: sh scripts/run_db_command.sh <POD_NAME>

## 7. Test if the applications work

The following pages should be accessible by web browser:

    http://localhost:30000/ - Frontend
    http://localhost:30003/ - Persons API
    http://localhost:30002/ - Connection API
    http://localhost:30005/ - Location API
    
