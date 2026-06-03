pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ecalcerrada/m17-actividad1-git:act3'
    }

    stages {

        stage('Limpieza workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout del código') {
            steps {
                checkout scm
            }
        }

        stage('Construir imagen Docker') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Probar contenedor') {
            steps {
                script {
                    sh """
                        docker run -d --name test_container ${DOCKER_IMAGE}
                        sleep 5
                        docker ps
                        docker stop test_container
                        docker rm test_container
                    """
                }
            }
        }

        stage('Push a Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push ${DOCKER_IMAGE}
                        docker logout
                    """
                }
            }
        }
    }

    post {
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}
