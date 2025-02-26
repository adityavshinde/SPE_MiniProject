pipeline {
    agent any
    triggers {
        githubPush()
    }
    environment {
        DOCKER_IMAGE_NAME = 'adityavshinde/calculator'
        GITHUB_REPO_URL = 'https://github.com/adityavshinde/SPE_MiniProject.git'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest test_calc.py --junitxml=report.xml'
                }
            }
            post {
                always {
                    junit 'report.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'DockerHubCred') {
                        sh "docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_IMAGE_NAME}:latest"
                        sh "docker push ${DOCKER_IMAGE_NAME}"
                    }
                }
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                script {
                    withEnv(["ANSIBLE_HOST_KEY_CHECKING=False"]) {
                        ansiblePlaybook(
                            playbook: 'myplaybook.yml',
                            inventory: 'inventory'
                        )
                    }
                }
            }
        }
    }

    post {
        success {
            mail to: 'AdityaVijay.Shinde@iiitb.ac.in',
                 subject: "Application Deployment SUCCESS: Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build was successful!"
        }
        failure {
            mail to: 'AdityaVijay.Shinde@iiitb.ac.in',
                 subject: "Application Deployment FAILURE: Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build failed."
        }
        always {
            cleanWs()
        }
    }
}

