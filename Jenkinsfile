pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/Molina211/Sexto-Semestre.git'
            }
        }

        stage('Backup de apuntes') {
            steps {
                script {
                    echo '🗂️ Haciendo copia de seguridad de los apuntes...'
                    def date = sh(script: "date +%Y-%m-%d_%H-%M-%S", returnStdout: true).trim()
                    def backupDir = "/var/jenkins_home/backups_apuntes/${date}"
                    sh """
                        mkdir -p ${backupDir}
                        cp -r * ${backupDir}/
                        echo '✅ Backup completado en ${backupDir}' > backup_log.txt
                    """
                }
            }
        }

        stage('Notificar por correo') {
            steps {
                emailext (
                    subject: "📚 Backup completado: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                        <h2>Repositorio de apuntes actualizado correctamente</h2>
                        <p><b>Job:</b> ${env.JOB_NAME}</p>
                        <p><b>Build:</b> #${env.BUILD_NUMBER}</p>
                        <p><b>Estado:</b> ${currentBuild.currentResult}</p>
                        <p>Ver detalles: <a href='${env.BUILD_URL}'>${env.BUILD_URL}</a></p>
                    """,
                    mimeType: 'text/html',
                    to: 'jhonmolina21109@gmail.com'
                )
            }
        }
    }
}
