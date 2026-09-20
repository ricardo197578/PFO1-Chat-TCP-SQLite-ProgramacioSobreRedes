
# PFO1 - Chat Cliente-Servidor con Python y SQLite

## 1. Descripción del proyecto

El presente proyecto consiste en el desarrollo de una aplicación
de chat cliente-servidor utilizando el lenguaje Python.

La comunicación se realiza mediante sockets TCP/IP.

El cliente permite enviar múltiples mensajes al servidor, que
los recibe, registra en una base de datos SQLite y devuelve
una confirmación con la fecha y hora de recepción.

El programa permite finalizar la conexión del cliente
escribiendo la palabra "éxito".

## 2. Tecnologías utilizadas

- Python 3.
- Biblioteca socket para la comunicación TCP/IP.
- Biblioteca sqlite3 para la gestión de la base de datos.
- Biblioteca datetime para registrar la fecha y hora.
- SQLite como sistema de almacenamiento de mensajes.

Todas las bibliotecas utilizadas forman parte de la
biblioteca estándar de Python.

No es necesario instalar dependencias externas.

## 3. Estructura del proyecto

```text
Chat_Cliente_Servidor/
│
├── servidor.py
├── cliente.py
├── database.py
├── ver_mensajes.py
├── README.md
└── .gitignore
```

Descripción de los archivos:

servidor.py:
Inicializa el servidor TCP, acepta conexiones,
recibe mensajes y coordina su almacenamiento.

cliente.py:
Establece la conexión TCP con el servidor,
envía mensajes y muestra las confirmaciones recibidas.

database.py:
Contiene las funciones necesarias para crear la
tabla de mensajes y almacenar los registros en SQLite.

ver_mensajes.py:
Permite consultar los mensajes almacenados
en la base de datos.

chat.db:
Archivo de la base de datos SQLite.

README.md:
Documentación e instrucciones de ejecución.

## 4. Configuración de la conexión

Dirección IP: 127.0.0.1

Puerto: 5000

Protocolo: TCP

La aplicación está configurada para ejecutarse
localmente en una misma computadora.

## 5. Ejecución del servidor

Abrir una terminal en la carpeta del proyecto.

Ejecutar el siguiente comando:

    python servidor.py

El servidor inicializa la base de datos,
crea la tabla de mensajes si no existe
y comienza a esperar conexiones.

Para detenerlo manualmente mientras espera
conexiones, presionar Ctrl + C.

## 6. Ejecución del cliente

Abrir una segunda terminal en la misma carpeta.

Ejecutar:

    python cliente.py

El cliente establece la conexión con el servidor.

Una vez conectado, permite escribir y enviar
múltiples mensajes.

Para finalizar la conexión, escribir:

    éxito

La palabra debe ingresarse sola y confirmarse
presionando Enter.

## 7. Almacenamiento de mensajes

Cada mensaje recibido se registra en SQLite.

La tabla mensajes contiene los siguientes campos:

id:
Identificador único del mensaje.

contenido:
Texto enviado por el cliente.

fecha_envio:
Fecha y hora en que el servidor procesa el mensaje.

ip_cliente:
Dirección IP del cliente que envió el mensaje.

El identificador se genera automáticamente.

Los mensajes permanecen almacenados después
de finalizar la ejecución del programa.

## 8. Confirmación de recepción

Después de almacenar correctamente un mensaje,
el servidor devuelve una confirmación al cliente.

Ejemplo:

    Mensaje recibido: 2026-09-20 18:30:00

La fecha y hora corresponden al momento en
que el servidor procesa el mensaje.

## 9. Consulta de los mensajes almacenados

Para visualizar los registros de la base de datos,
ejecutar:

    python ver_mensajes.py

El programa consulta la tabla mensajes y muestra
los registros almacenados.

## 10. Manejo de errores

El programa contempla las siguientes situaciones:

- Servidor no disponible.
- Puerto de comunicación ocupado.
- Problemas de acceso a la base de datos SQLite.
- Errores de comunicación mediante sockets.

El servidor permite detener su ejecución mediante
Ctrl + C mientras espera nuevas conexiones.

## 11. Pruebas realizadas

Se realizaron pruebas de:

- Inicio del servidor TCP.
- Conexión del cliente con el servidor.
- Envío y recepción de múltiples mensajes.
- Confirmación de recepción con fecha y hora.
- Almacenamiento de mensajes en SQLite.
- Consulta de los registros almacenados.
- Finalización del cliente mediante la palabra éxito.
- Cierre manual del servidor con Ctrl + C.
- Conexiones sucesivas sin reiniciar el servidor.

## 12. Autor

Nombre y apellido: [Ricardo Cesar Canteros]

Materia: Programación sobre Redes

Trabajo práctico: PFO1

Año: 2026