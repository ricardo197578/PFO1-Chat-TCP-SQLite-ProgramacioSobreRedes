
import sqlite3
from datetime import datetime

# Nombre del archivo de la base de datos
NOMBRE_DB = "chat.db"


# Función para crear la tabla de mensajes
def crear_tabla():

    # Establecemos la conexión con SQLite
    conexion = sqlite3.connect(NOMBRE_DB)

    try:
        # Creamos un cursor para ejecutar instrucciones SQL
        cursor = conexion.cursor()

        # Creamos la tabla si todavía no existe
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL,
                fecha_envio TEXT NOT NULL,
                ip_cliente TEXT NOT NULL
            )
        """)

        # Confirmamos los cambios
        conexion.commit()

        print("Tabla de mensajes creada correctamente.")

    finally:
        # Cerramos la conexión con la base de datos
        conexion.close()


# Función para guardar un mensaje en SQLite
def guardar_mensaje(contenido, fecha_envio, ip_cliente):

    # Establecemos la conexión con la base de datos
    conexion = sqlite3.connect(NOMBRE_DB)

    try:
        # Creamos un cursor
        cursor = conexion.cursor()

        # Insertamos el mensaje en la tabla
        cursor.execute("""
            INSERT INTO mensajes
            (contenido, fecha_envio, ip_cliente)
            VALUES (?, ?, ?)
        """, (contenido, fecha_envio, ip_cliente))

        # Confirmamos la inserción
        conexion.commit()

        print("Mensaje guardado correctamente.")

    finally:
        # Cerramos la conexión
        conexion.close()

# Ejecutamos la función
# crear_tabla()


# Este bloque se ejecuta al iniciar database.py directamente
if __name__ == "__main__":

    # Creamos la tabla si todavía no existe
    crear_tabla()

    # Obtenemos la fecha y hora actuales
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardamos un mensaje de prueba
    guardar_mensaje(
        "Hola, este es mi primer mensaje",
        fecha_actual,
        "127.0.0.1"
    )