import network
import socket

# ==== CONFIGURAR EL ESP32 COMO ACCESS POINT ====
ap = network.WLAN(network.AP_IF)
ap.active(True)

# Nombre de la red WiFi y contraseña
ap.config(essid="Brayan y molina", password="12345678")

print("Punto de acceso creado ✅")
print("Red WiFi:", ap.config('essid'))
print("Contraseña:", "12345678")
print("Dirección IP:", ap.ifconfig()[0])

# ==== PÁGINA HTML EDUCATIVA ====
pagina = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Bienvenido al ESP32</title>
  <style>
    body { font-family: Arial; background: #f4f4f9; color: #333; text-align: center; }
    h1 { color: #1565c0; }
    p { font-size: 18px; }
  </style>
</head>
<body>
  <h1>🌐 Red WiFi del ESP32</h1>
  <p>Te has conectado exitosamente a la red educativa del ESP32.</p>
  <p>Aquí puedes aprender sobre <b>microcontroladores</b> y <b>servidores web</b>.</p>
  <footer style="margin-top:20px;color:gray;">© 2025 - Servido desde ESP32</footer>
</body>
</html>
"""

# ==== SERVIDOR WEB ====
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Servidor web activo en: http://", ap.ifconfig()[0])

while True:
    cl, addr = s.accept()
    print("Cliente conectado desde:", addr)
    cl.recv(1024)  # Se recibe la petición HTTP
    cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    cl.sendall(pagina)
    cl.close()
