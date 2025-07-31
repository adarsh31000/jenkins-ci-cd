pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-username/todo-app.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    dockerImage = docker.build("todo-app")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    dockerImage.run("-d -p 5000:5000")
                }
            }
        }
    }
}
