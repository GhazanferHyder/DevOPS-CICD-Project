pipeline {
    agent any

    environment {
        IMAGE_NAME = "ghazan011/flask-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

       

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {

                    sh '''
                    echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh """
                docker push ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

    }

    post {

        always {
            sh 'docker logout || true'
        }

        success {
            echo "Pipeline completed successfully."
        }

        failure {
            echo "Pipeline failed."
        }

    }
}