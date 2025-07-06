pipeline {
    agent any

    environment {
        IMAGE_NAME = "insureme-app"
        TEST_SERVER = "ubuntu@<test-server-ip>"
        PROD_SERVER = "ubuntu@<prod-server-ip>"
        PRIVATE_KEY = credentials('ec2-ssh-key')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/abhinav-saraf/star-agile-insurance-project.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Docker Build') {
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
                sh 'scp -i $PRIVATE_KEY docker-compose.yml $TEST_SERVER:/home/ubuntu/'
                ssh '-i $PRIVATE_KEY $TEST_SERVER "docker-compose down && docker-compose up -d"'
            }
        }

        stage('Selenium Test') {
            steps {
                sh 'pytest tests/selenium_test.py'
            }
        }

        stage('Deploy to Prod') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS'}
            }
            steps {
                sh 'scp -i $PRIVATE_KEY docker-compose.yml $PROD_SERVER:/home/ubuntu/'
                sh 'ssh -i $PRIVATE_KEY $PROD_SERVER "docker-compose down && docker-compose up -d"'
            }
        }
    }
