pipeline {
    agent any

    environment {
        IMAGE_NAME = "insuranceme-app"
        DOCKERHUB_USER = "sarafabhinav1997"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/abhinav-saraf/star-agile-insurance-project.git'
            }
        }

        stage('Build with Maven') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker tag $IMAGE_NAME $DOCKERHUB_USER/$IMAGE_NAME:latest'
                    sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:latest'
                }
            }
        }

      stage('Deploy to Test Server') {
            steps {
                sh 'ansible-playbook -i ansible/inventory/test ansible/playbooks/deploy.yml'
            }
        }

        stage('Selenium Tests') {
            steps {
                sh 'python3 tests/selenium_test.py'
            }
        }

        stage('Manual Approval for Prod?') {
            steps {
                input message: 'Promote to production?'
            }
        }
   
        stage('Deploy to Prod Server') {
            when {
                expression {
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                sh 'ansible-playbook -i ansible/inventory/prod ansible/playbooks/deploy.yml'
            }
        }
    }
