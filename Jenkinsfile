pipeline {
    agent any
    stages {
        stage('Python :: Installing Requirements'){
            steps {
                    sh 'pip install -r requirements.txt'
                }
            }

        stage('Python :: Build docker' ){
            steps{
                    sh 'docker build -t my-new-python .'
                }
            }

        stage('Python :: Run docker' ){
            steps{
                    sh 'docker run --name appy -d --rm -p 4200:80 my-new-python'
                }
            }
  }
}