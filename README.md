Start all instances including aks cluster

- terraform apply

  Connect to Azure

- az login

  Connect to CR

- az acr login -n {Name of Azure CR}

  Get credentials and kubectl configuration

- az aks get-credentials --resource-group {resource Group} --name {name of aks cluster}

  Install kubeflow

- kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
- kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
- kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/dev?ref=$PIPELINE_VERSION"

  Set the kubectl context to the aks cluster

- kubectl get configmap -n kubeflow
- kubectl edit configmap CONFIGMAP_NAME -n kubeflow

Connect AKS with ACR

-az aks update -n wiredibexaks1 -g resourceGroup --attach-acr wiredibexacr

Change the containerregistry name

- zenml container-registry update cloud_registry --uri=$PATH_TO_YOUR_CONTAINER_REGISTRY
- zenml artifact-store update cloud_artifact_store --path=$PATH_TO_YOUR_BUCKET
- zenml orchestrator update cloud_orchestrator --kubernetes_context={the kubernetes context}

  View the dashboard

- kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
