# Gopher_smtp
Este código crea un servidor HTTP simple que responde a las solicitudes GET e intenta enviar un correo a un servidor remoto utilizando la técnica "gopher". La técnica de "gopher" se utiliza para construir URLs engañosas y aprovechar vulnerabilidades en servidores mal configurados.
### Ejemplo de ejecucion 
Con nc nos ponemos en escucha para resivir la coneccion generada por el archivo .odt con la macro maliciosa.
❯ nc -lnvp 4443
Ejecutamos el script que se encargara de montar el servidor exponer el archivo .odt y enviar el correo.
❯ python3 gopher_smtp.py

´El script requiere cambios para funcionar segun su ip, puerto, nombre del archivo .odt, nc en escucha´
`Este es un ejemplo práctico en un entorno de laboratorio controlado que tiene como objetivo demostrar las posibles consecuencias de la ejecución de macros y una configuración deficiente de servidores, así como la falta de seguridad en los servidores de correo (MX)`
