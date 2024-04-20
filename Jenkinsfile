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
                dir('flask-web-app') {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Flask Application') {
            steps {
                dir('flask-web-app') {
                    sh 'python app.py'
                }
            }
        }
    }
}

