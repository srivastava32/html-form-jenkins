
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\Naman Srivastava\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" --version'
            }
        }

        stage('Test HTML Form') {
            steps {
                bat '"C:\\Users\\Naman Srivastava\\AppData\\Local\\Programs\\Python\\Python315\\python.exe" -m unittest discover -s tests -p "test*.py" -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML Form Tests Passed!'
        }

        failure {
            echo 'FAILURE: HTML Form Pipeline Failed!'
        }

        always {
            echo 'HTML Form Pipeline Execution Completed.'
        }
    }
}
