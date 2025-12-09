pipeline {

    agent any

    environment {
        IMAGE_NAME = "hrishi-flask"
        IMAGE_TAG  = "v1"
        DOCKERHUB_USER = "hrishi001"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Fetching code from Jenkins workspace..."
                git branch: 'main', url: 'https://github.com/Hrishikesh009/flask-redis-cicd.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python dependencies..."
                sh 'pip install -r app/requirements.txt || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh """
                    docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ./app
                """
            }
        }
	
	stage('Push to DockerHub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKERHUB_PASS')]) {
                    sh """
                        echo \$DOCKERHUB_PASS | docker login -u ${DOCKERHUB_USER} --password-stdin
                        docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "Running container from built image..."
		 sh """
                    docker run -d --name flask_cicd -p 5000:5000 ${DOCKERHUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} || true
                """
            }
        }
    }

    post {

        always {
            echo "Cleaning up old containers..."
            sh "docker rm -f flask_cicd || true"
        }
    }
}
