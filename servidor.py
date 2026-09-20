
# Importamos los módulos necesarios
import socket
import sqlite3

from datetime import datetime

# Importamos las funciones de la base de datos
from database import crear_tabla, guardar_mensaje


# Configuración del servidor
HOST = "127.0.0.1"
PUERTO = 5000


# Función para inicializar el servidor TCP
def inicializar_servidor():

    # Creamos el socket TCP/IP
    servidor = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        # Asociamos el socket a la IP y al puerto
        servidor.bind((HOST, PUERTO))

        # Ponemos el servidor en modo escucha
        servidor.listen(1)

        # Timeout solamente para aceptar conexiones
        servidor.settimeout(1.0)

        print("Servidor iniciado correctamente.")
        print(f"Esperando conexiones en {HOST}:{PUERTO}")
        print("Presioná Ctrl + C para detener el servidor.")

        return servidor

    except OSError:

        servidor.close()
        raise


# Función para atender los mensajes de un cliente
def atender_cliente(conexion, direccion):

    # Obtenemos la dirección IP del cliente
    ip_cliente = direccion[0]

    print(f"Cliente conectado desde: {direccion}")

    # Creamos una interfaz para leer mensajes por línea
    archivo = conexion.makefile("rb")

    try:

        # Bucle para recibir múltiples mensajes
        while True:

            # Leemos un mensaje completo
            datos = archivo.readline()

            # Verificamos si el cliente se desconectó
            if not datos:

                print("El cliente se desconectó.")
                break

            # Convertimos los bytes recibidos a texto
            mensaje = datos.decode("utf-8").rstrip("\r\n")

            print(f"Mensaje recibido: {mensaje}")

            # Obtenemos la fecha y hora actuales
            fecha_envio = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            # Intentamos guardar el mensaje en SQLite
            try:

                guardar_mensaje(
                    mensaje,
                    fecha_envio,
                    ip_cliente
                )

            except sqlite3.Error as error:

                print(f"Error de base de datos: {error}")

                # Informamos al cliente que no se pudo guardar
                respuesta = "ERROR: No se pudo guardar el mensaje"

                conexion.sendall(
                    (respuesta + "\n").encode("utf-8")
                )

                continue

            # Preparamos la confirmación
            respuesta = f"Mensaje recibido: {fecha_envio}"

            # Enviamos la confirmación al cliente
            conexion.sendall(
                (respuesta + "\n").encode("utf-8")
            )

    except (OSError, UnicodeError) as error:

        print(f"Error de comunicación: {error}")

    finally:

        # Cerramos la interfaz de lectura
        archivo.close()


# Función principal del programa
def main():

    servidor = None

    try:

        # Creamos la tabla de mensajes
        crear_tabla()

        # Inicializamos el servidor
        servidor = inicializar_servidor()

        # Bucle principal para aceptar conexiones
        while True:

            try:

                # Esperamos una nueva conexión
                conexion, direccion = servidor.accept()

            except socket.timeout:

                # Volvemos a esperar conexiones
                continue

            try:

                # Atendemos los mensajes del cliente
                atender_cliente(conexion, direccion)

            finally:

                # Cerramos la conexión con el cliente
                conexion.close()

    except sqlite3.Error as error:

        print(f"Error al acceder a la base de datos: {error}")

    except KeyboardInterrupt:

        print("\nServidor detenido por el usuario.")

    except OSError as error:

        # Error 10048: dirección en uso en Windows
        # Error 98: dirección en uso en Linux
        if getattr(error, "errno", None) in (98, 10048) or \
           getattr(error, "winerror", None) == 10048:

            print("Error: el puerto 5000 ya está ocupado.")

        else:

            print(f"Error del servidor: {error}")

    finally:

        # Cerramos el socket principal
        if servidor is not None:
            servidor.close()

        print("Servidor finalizado.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()