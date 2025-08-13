pipeline {
    agent {
        docker {
            image 'docker:27.3.1'
            args '-u root --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /home/soso/PycharmProjects/doker_test/dok_test:/code'
        }
    }
    environment {
        HOME = "${WORKSPACE}"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/soslan94/doker-test.git'
            }
        }
        stage('Check Python version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install --user --upgrade pip'
                sh 'pip install --user -r requirements.txt || echo "No requirements.txt found"'
            }
        }
        stage('Run script') {
            steps {
                sh 'echo "print(\'Hello from Jenkins inside Docker\')" > test.py'
                sh 'python3 test.py'
            }
        }
        stage('Install Docker Compose') {
            steps {
                sh '''
                    apk add --no-cache python3 py3-pip
                    pip3 install --user docker-compose
                '''
            }
        }
        stage('Build Docker Compose') {
            steps {
                dir('/code') {
                    sh 'docker-compose build'
                }
            }
        }
        stage('Deploy Docker Compose') {
            steps {
                dir('/code') {
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}