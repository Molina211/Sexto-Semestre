pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                echo '📦 Clonando el repositorio de apuntes...'
                git branch: 'main', url: 'https://github.com/Molina211/Sexto-Semestre.git'
            }
        }

        stage('Backup de apuntes') {
            steps {
                script {
                    echo '🗂️ Haciendo copia de seguridad de los apuntes...'
                    // Crear carpeta de backup con marca de tiempo
                    def date = sh(script: "date +%Y-%m-%d_%H-%M-%S", returnStdout: true).trim()
                    def backupDir = "/var/jenkins_home/backups_apuntes/${date}"
                    sh """
                        mkdir -p ${backupDir}
                        cp -r * ${backupDir}/
                        echo '✅ Backup completado en ${backupDir}' > backup_log.txt
                    """
                    echo "✅ Backup completado en: ${backupDir}"
                }
            }
        }

        stage('Notificar por correo') {
            steps {
                emailext (
                    subject: "📚 Informe - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                        <html>
                        <head>
                            <style>
                                body {
                                    font-family: 'Segoe UI', Arial, sans-serif;
                                    background-color: #f4f4f9;
                                    color: #333;
                                    padding: 20px;
                                }
                                .container {
                                    background: white;
                                    border-radius: 10px;
                                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                                    padding: 20px;
                                    max-width: 600px;
                                    margin: auto;
                                }
                                h2 {
                                    color: #0056b3;
                                    border-bottom: 2px solid #0056b3;
                                    padding-bottom: 10px;
                                }
                                .status {
                                    font-size: 18px;
                                    font-weight: bold;
                                    color: ${currentBuild.currentResult == 'SUCCESS' ? '#28a745' : '#dc3545'};
                                }
                                .info {
                                    margin: 10px 0;
                                }
                                .footer {
                                    margin-top: 20px;
                                    font-size: 12px;
                                    color: #888;
                                    text-align: center;
                                }
                                a.button {
                                    display: inline-block;
                                    padding: 10px 15px;
                                    background-color: #007bff;
                                    color: white;
                                    text-decoration: none;
                                    border-radius: 5px;
                                    margin-top: 15px;
                                }
                                a.button:hover {
                                    background-color: #0056b3;
                                }
                            </style>
                        </head>
                        <body>
                            <div class="container">
                                <h2>📘 Backup de apuntes completado</h2>
                                <p class="info"><b>Job:</b> ${env.JOB_NAME}</p>
                                <p class="info"><b>Build:</b> #${env.BUILD_NUMBER}</p>
                                <p class="info"><b>Estado:</b> <span class="status">${currentBuild.currentResult}</span></p>
                                <p class="info"><b>Repositorio:</b> ${env.GIT_URL ?: 'No especificado'}</p>
                                <a class="button" href="${env.BUILD_URL}">🔍 Ver detalles del build</a>
                                <div class="footer">
                                    <p>Notificación automática generada por Jenkins 📬</p>
                                </div>
                            </div>
                        </body>
                        </html>
                    """,
                    mimeType: 'text/html',
                    to: 'jhonmolina21109@gmail.com'
                )
            }
        }
    }
}
