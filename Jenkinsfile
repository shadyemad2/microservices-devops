pipeline {
    agent any

    environment {
        BACKEND_IMAGE = "shadyemad/blog-backend"
        FRONTEND_IMAGE = "shadyemad/blog-frontend"
        VERSION = "v1.0.${BUILD_NUMBER}"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/shadyemad2/microservices-devops.git'
            }
        }

        stage('Build & Push Backend Image') {
            steps {
                dir('app/backend') {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-reg', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            docker build -t ${BACKEND_IMAGE}:${VERSION} .
                            echo "${DOCKER_PASS}" | docker login -u "${DOCKER_USER}" --password-stdin
                            docker push ${BACKEND_IMAGE}:${VERSION}
                        '''
                    }
                }
            }
        }

        stage('Build & Push Frontend Image') {
            steps {
                dir('app/frontend') {
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-reg', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            docker build -t ${FRONTEND_IMAGE}:${VERSION} .
                            echo "${DOCKER_PASS}" | docker login -u "${DOCKER_USER}" --password-stdin
                            docker push ${FRONTEND_IMAGE}:${VERSION}
                        '''
                    }
                }
            }
        }

        stage('Update Helm values') {
            steps {
                sh '''
                    sed -i "s|tag:.*|tag: \\"${VERSION}\\"|g" helm-charts/backend/values.yaml
                    sed -i "s|tag:.*|tag: \\"${VERSION}\\"|g" helm-charts/frontend/values.yaml
                '''
            }
        }

        stage('Commit & Push Changes') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    sh '''
                        git config user.email "ci@auto.dev"
                        git config user.name "CI Bot"
                        git add helm-charts/backend/values.yaml helm-charts/frontend/values.yaml || true
                        git commit -m "Update image tags to ${VERSION} [CI]" || true

                        git pull --rebase origin main || true
                        git push https://${GIT_USER}:${GIT_PASS}@github.com/shadyemad2/microservices-devops.git HEAD:main

                        git pull --rebase origin main || true
                        git push https://${GIT_USER}:${GIT_PASS}@github.com/shadyemad2/microservices-devops.git HEAD:main
                    '''
                }
            }
        }
    }
}

