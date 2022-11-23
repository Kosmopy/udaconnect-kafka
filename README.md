# udaconnect-kafka

[MISSING]

##How to set up Kafka in Kubernetes

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


[MISSING]
