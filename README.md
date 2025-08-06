# 🛠️ Microservices DevOps Project - Blog App

This is a complete **DevOps microservices project** demonstrating a CI/CD pipeline using **Jenkins**, **Docker**, **Helm**, and **ArgoCD** to deploy a blog application (backend + frontend + database) on a Kubernetes cluster.

---

## 📦 Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML/CSS/JS
- **Database**: PostgreSQL
- **CI/CD**: Jenkins + Docker + Helm + ArgoCD
- **Container Registry**: Docker Hub
- **Kubernetes**: Local cluster (Minikube / kubeadm)
- **Monitoring**: Prometheus + Grafana

---

## 📸 Project Architecture

<!-- Add screenshot here (e.g., architecture diagram) -->

---

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

<!-- Add screenshot of Jenkins pipeline here -->

---

## 🚢 ArgoCD GitOps Deployment

ArgoCD continuously monitors the Git repository for changes to Helm charts and syncs the Kubernetes cluster accordingly.

- ArgoCD UI shows app status and sync status.
- You can rollback or redeploy from ArgoCD.

<!-- Add screenshot of ArgoCD app here -->

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

## 🗃️ Future Improvements

- Add unit tests & automated test stage in Jenkins.
- Enable Slack notifications on pipeline events.
- Add Ingress controller (e.g., NGINX).
- Add production-grade secrets management (e.g., Vault or Sealed Secrets).
- Configure Horizontal Pod Autoscaler (HPA).

---

## 🙌 Author

**Shady Emad Wahib Farhat**

DevOps | Linux | Kubernetes | Cloud Enthusiast  
[LinkedIn Profile](https://www.linkedin.com/in/shadyemad)  
[GitHub Profile](https://github.com/shadyemad)

---

## 📷 Screenshots

> Replace below with actual screenshots:

- ![Architecture Diagram](screenshots/architecture.png)
- ![Jenkins Pipeline](screenshots/jenkins-pipeline.png)
- ![ArgoCD App](screenshots/argocd-app.png)
- ![Grafana Dashboard](screenshots/grafana-dashboard.png)

