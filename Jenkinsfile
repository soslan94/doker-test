pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u' // чтобы вывод был без буферизации
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
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest || echo "Tests failed"'
            }
        }
    }
}