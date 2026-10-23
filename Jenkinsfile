

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
                bat '"C:\\Users\\Naman Srivastava\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\python.exe" --version'
                bat '"C:\\Users\\Naman Srivastava\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\python.exe" -m unittest discover -s tests -p "test*.py" -v'
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

