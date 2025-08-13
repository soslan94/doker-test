pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/soslan94/doker-test.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt || echo "No requirements.txt found"'
            }
        }
    }
}