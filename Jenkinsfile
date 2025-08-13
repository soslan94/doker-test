pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/soslan94/doker-test.git'
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
            }
        }
    }
}