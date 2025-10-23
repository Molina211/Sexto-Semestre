pipeline {
  agent any

  environment {
    TRELLO_KEY = credentials('TRELLO_KEY')
    TRELLO_TOKEN = credentials('TRELLO_TOKEN')
    CARD_ID = '68f9ce9f8565d3e52ea65b24'   // ID de tu tarjeta Trello
    LIST_DONE = '68f9ce8023003213ed1fe16a' // ID de la lista "Hecho"
  }

  stages {
    stage('Build') {
      steps {
        echo "🛠️ Construyendo proyecto..."
      }
    }

    stage('Test') {
      steps {
        echo "🧪 Ejecutando pruebas..."
      }
    }
  }

  post {
    success {
      echo "✅ Build exitoso, moviendo tarjeta a Hecho..."
      sh '''
        curl -X PUT \
          "https://api.trello.com/1/cards/${CARD_ID}?key=${TRELLO_KEY}&token=${TRELLO_TOKEN}&idList=${LIST_DONE}"
      '''
    }
    failure {
      echo "❌ Build falló, comentando en la tarjeta..."
      sh '''
        curl -X POST \
          "https://api.trello.com/1/cards/${CARD_ID}/actions/comments?key=${TRELLO_KEY}&token=${TRELLO_TOKEN}" \
          -d "text=El build en Jenkins falló. Revisa los logs en ${BUILD_URL}."
      '''
    }
  }
}
