pipeline {
    agent any

    environment {
        IMAGE_NAME = "insureme-app"
        TF_WORKSPACE = "test"
        ANSIBLE_HOST_KEY_CHECKING = "False"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/abhinav-saraf/star-agile-insurance-project.git'
            }
        }

        stage('Maven Package') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker tag $IMAGE_NAME sarafabhinav1997/$IMAGE_NAME:latest'
                    sh 'docker push sarafabhinav1997/$IMAGE_NAME:latest'
                }
            }
        }

      stage('Deploy to Test') {
            steps {
                sh 'ansible-playbook -i ansible/test ansible/deploy.yml'
            }
        }

        stage('Deploy to Prod') {
            when {
                expression {currentBuild.result == null || currentBuild.result == 'SUCCESS'}
            }
            steps {
                sh 'ansible-playbook -i ansible/prod ansible/deploy.yml'
            }
        }
    }
}
