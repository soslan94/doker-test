pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root --privileged -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/code'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/soslan94/doker-test.git'
            }
        }
        stage('Check Python version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt || echo "No requirements.txt found"'
            }
        }
        stage('Run script') {
            steps {
                sh 'echo "print(\'Hello from Jenkins inside Python 3.11\')" > test.py'
                sh 'python test.py'
            }
        }
        stage('Install Docker Compose') {
            steps {
                sh 'apt update && apt install -y docker.io'
                sh 'pip install docker-compose'
            }
        }
        stage('Build Docker Compose') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Deploy Docker Compose') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}