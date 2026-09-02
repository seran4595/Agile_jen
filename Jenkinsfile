pipeline{
    agent any
    stages{
        stage('checkout Code'){
            steps{
                git branch:'main',
                url:'https://github.com/seran4595/Agile_jen.git'
            }
        }
        stage('Build'){
            steps{
                bat'python app.py 20 5'
            }
        }
    }
}