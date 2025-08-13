pipeline {
    agent {
        docker {
            image 'docker:27.3.1'
            args '-u root --privileged -v /var/run/docker.sock:/var/run/docker.sock -v /home/soso/PycharmProjects/doker_test/dok_test:/code'
        }
    }
    environment {
        HOME = "${WORKSPACE}"
        PATH = "${WORKSPACE}/venv/bin:/usr/local/bin:/usr/bin:/bin"
    }
    stages {
        stage('Setup Environment') {
            steps {
                sh '''
                    apk add --no-cache python3 py3-pip git
                    python3 --version
                    python3 -m venv $WORKSPACE/venv
                    . $WORKSPACE/venv/bin/activate
                    pip install --upgrade pip
                    pip install docker-compose
                    docker-compose --version
                '''
            }
        }
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/soslan94/doker-test.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                    . $WORKSPACE/venv/bin/activate
                    pip install -r requirements.txt || echo "No requirements.txt found"
                '''
            }
        }
        stage('Run script') {
            steps {
                sh '''
                    . $WORKSPACE/venv/bin/activate
                    echo "print('Hello from Jenkins inside Docker')" > test.py
                    python test.py
                '''
            }
        }
        stage('Build Docker Compose') {
            steps {
                dir('/code') {
                    sh '''
                        . $WORKSPACE/venv/bin/activate
                        docker-compose build
                    '''
                }
            }
        }
        stage('Deploy Docker Compose') {
            steps {
                dir('/code') {
                    sh '''
                        . $WORKSPACE/venv/bin/activate
                        docker-compose up -d
                    '''
                }
            }
        }
    }
}