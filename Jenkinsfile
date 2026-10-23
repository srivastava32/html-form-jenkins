

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
                bat 'python -m unittest discover -s tests -v'
            }
        }
    }

    post {
        success {
            echo 'HTML Form Tests Passed!'
        }
        failure {
            echo 'HTML Form Tests Failed!'
        }
    }
}

