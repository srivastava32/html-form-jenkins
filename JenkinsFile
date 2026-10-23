
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test HTML Form') {
            steps {
                sh 'python3 -m unittest discover -s tests -v'
            }
        }
    }
}
