pipeline {
    agent any
    triggers {
        githubPush()
    }
    environment {
	PATH = "${env.PATH}:/var/lib/jenkins/.local/bin"
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

        stage('Setup Python') {
            steps {
                script {
                    sh 'python3 --version || exit 1'
                    sh 'pip install --upgrade pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'pytest test_calc.py --junitxml=test-results.xml || true'
                }
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE_NAME} .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'DockerHubCred') {
                        sh 'docker tag calculator adityavshinde/calculator:latest'
                        sh 'docker push adityavshinde/calculator'
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
                 subject: "SUCCESS: Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build was successful!"
        }
        failure {
            mail to: 'AdityaVijay.Shinde@iiitb.ac.in',
                 subject: "FAILURE: Build ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "The build failed. Check logs."
        }
        always {
            cleanWs()
        }
    }
}

