pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                checkout scm
                sh 'docker compose down'
                sh 'docker compose pull'
                sh 'docker compose up -d'
            }
        }
    }
}
