pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/joshkr1/flask-web-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('/home/centos/flask-web-app/') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        // Additional stages...
    }
}

