
# Importamos el módulo socket
import socket



# Configuración del servidor
HOST = "127.0.0.1"
PUERTO = 5000


# Función principal del cliente
def main():

    # Creamos el socket TCP/IP
    cliente = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:

        # Establecemos la conexión con el servidor
        cliente.connect((HOST, PUERTO))

        print("Conectado al servidor.")
        print("Escribí 'éxito' para finalizar el chat.")

        # Creamos una interfaz para leer las respuestas
        archivo = cliente.makefile("rb")

        try:

            # Bucle para enviar múltiples mensajes
            while True:

                # Solicitamos un mensaje al usuario
                mensaje = input("Escribí un mensaje: ")

                # Verificamos si desea finalizar
                if mensaje == "éxito":
                    break

                # Agregamos un salto de línea al mensaje
                datos = (mensaje + "\n").encode("utf-8")

                # Enviamos el mensaje al servidor
                cliente.sendall(datos)

                # Recibimos la respuesta del servidor
                respuesta = archivo.readline()

                # Verificamos si se cerró la conexión
                if not respuesta:

                    print("El servidor cerró la conexión.")
                    break

                # Convertimos la respuesta a texto
                texto = respuesta.decode("utf-8").rstrip("\r\n")

                # Mostramos la respuesta recibida
                print(f"Respuesta del servidor: {texto}")

        finally:

            # Cerramos la interfaz de lectura
            archivo.close()

    except ConnectionRefusedError:

        print("Error: no se pudo conectar con el servidor.")
        print("Verificá que servidor.py esté ejecutándose.")

    except (OSError, UnicodeError) as error:

        print(f"Error de comunicación: {error}")

    except KeyboardInterrupt:

        print("\nCliente detenido por el usuario.")

    finally:

        # Cerramos el socket del cliente
        cliente.close()

        print("Cliente finalizado.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()