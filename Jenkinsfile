pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/adityavshinde/SPE_MiniProject.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_calc.py'
            }
        }

        stage('Build Artifact') {
            steps {
                sh 'tar -cvf calculator.tar calc.py'
            }
        }
    }
}
