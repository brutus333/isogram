pipeline {
  agent {
    docker {
      image 'python:3.6.4-jessie'
    }
    
  }
  stages {
    stage('Unit test') {
      steps {
        sh '''env
pip install -U pytest
pytest .'''
      }
    }
  }
  environment {
    http_proxy = '${http_proxy}'
    https_proxy = '${https_proxy}'
  }
}