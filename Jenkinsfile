
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }

        stage('Run Login Test') {
            steps {
                sh 'mkdir -p reports'
                sh '.venv/bin/python -m pytest tests/test_login.py -v --junitxml=reports/junit.xml --html=reports/report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit.xml', allowEmptyResults: true
            archiveArtifacts artifacts: 'reports/*.html,reports/*.xml', allowEmptyArchive: true
        }
    }
}
