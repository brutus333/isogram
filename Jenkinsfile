pipeline {
  agent {
    docker {
      image 'python:3.6.4-jessie'
      args '-e http_proxy=${http_proxy} -e https_proxy=${https_proxy}'
    }
    
  }
  stages {
    stage('Install prereq') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Unit test') {
      steps {
        sh 'pytest .'
      }
    }
  }
}