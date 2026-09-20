
import sqlite3

# Nos conectamos a la base de datos
conexion = sqlite3.connect("chat.db")

try:
    # Creamos un cursor
    cursor = conexion.cursor()

    # Consultamos todos los mensajes
    cursor.execute("SELECT * FROM mensajes")

    # Obtenemos los registros
    mensajes = cursor.fetchall()

    # Mostramos los mensajes guardados
    for mensaje in mensajes:
        print(mensaje)

finally:
    # Cerramos la conexión
    conexion.close()