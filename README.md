# 🛠️ Microservices DevOps Project - Blog App

This is a complete **DevOps microservices project** demonstrating a CI/CD pipeline using **Jenkins**, **Docker**, **Helm**, and **ArgoCD** to deploy a blog application (backend + frontend + database) on a Kubernetes cluster.

---
<img width="1018" height="432" alt="overview" src="https://github.com/user-attachments/assets/59cbcf7f-7527-45b0-ba12-428da26ea193" />

## 📦 Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML/CSS/JS
- **Database**: PostgreSQL
- **CI/CD**: Jenkins + Docker + Helm + ArgoCD
- **Container Registry**: Docker Hub
- **Kubernetes**: Local cluster (Minikube)
- **Monitoring**: Prometheus + Grafana


## 🚀 Project Features

- Full microservices deployment with backend, frontend, and PostgreSQL.
- CI/CD Pipeline using Jenkins with automatic:
  - Code checkout
  - Docker image build and push
  - Helm values update
  - Git commit and push
- GitOps deployment using **ArgoCD**.
- Version tagging with build numbers.
- Monitoring with Prometheus and Grafana dashboards.

---

## 📁 Folder Structure

```bash
microservices-devops/
├── app/
│   ├── backend/
│   └── frontend/
├── argocd/
│   ├── backend.yaml
│   ├── frontend.yaml
│   └── database.yaml
├── helm-charts/
│   ├── backend/
│   ├── frontend/
│   └── database/
├── jenkinsfile
```

---

## ⚙️ Jenkins CI/CD Pipeline

Jenkins is used to automate the CI/CD process:

1. **Code Checkout**: Pulls the latest code from GitHub.
2. **Docker Build & Push**: Builds the Docker image for each service and pushes it to Docker Hub.
3. **Helm Update**: Modifies the `values.yaml` files with new image tags.
4. **Git Commit**: Pushes updated Helm charts to Git (used by ArgoCD).
5. **Trigger ArgoCD**: ArgoCD detects changes and deploys automatically.

<img width="1846" height="858" alt="jenkins" src="https://github.com/user-attachments/assets/7a998be0-3257-4946-8b9f-feb35cf0ce21" />


---

## 🚢 ArgoCD GitOps Deployment

ArgoCD continuously monitors the Git repository for changes to Helm charts and syncs the Kubernetes cluster accordingly.

- ArgoCD UI shows app status and sync status.
- You can rollback or redeploy from ArgoCD.

<img width="1842" height="809" alt="argocd" src="https://github.com/user-attachments/assets/4371f122-7265-40af-b589-768c787cce80" />
<img width="1229" height="485" alt="argocd-pods" src="https://github.com/user-attachments/assets/d7f60fdc-c08f-43b0-8dfd-175a012e2fab" />

---

## 📊 Monitoring with Prometheus & Grafana

- Prometheus collects metrics from the Kubernetes cluster.
- Grafana visualizes those metrics via dashboards.
- Dashboards include:
  - CPU/Memory usage for each pod.
  - Request per second.
  - Health status of services.

<!-- Add screenshot of Grafana dashboards here -->

---

## 📷 Screenshots

- <img width="1307" height="740" alt="frontend" src="https://github.com/user-attachments/assets/60c2f26e-02ea-45f5-a9df-7477966322ea" />
- <img width="1270" height="713" alt="backend" src="https://github.com/user-attachments/assets/cc53f0be-3e2c-4566-b2e5-3afc47f70ac2" />

## 🧪 How to Run Locally

> Requirements: Minikube OR kubeadm cluster, Docker, Helm, Jenkins, ArgoCD

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/microservices-devops.git
   cd microservices-devops
   ```

2. Install Jenkins and configure pipeline.

3. Setup Docker and connect to Docker Hub.

4. Configure ArgoCD to watch `helm-charts/` directory.

5. Access ArgoCD and Grafana UIs via NodePort.


---

## 🙌 Author

**Shady Emad Wahib Farhat**

DevOps | Linux | Kubernetes | Cloud Enthusiast  
[LinkedIn Profile](https://www.linkedin.com/in/shadyemad)  
[GitHub Profile](https://github.com/shadyemad)

---




