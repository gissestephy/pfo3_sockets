import socket
import json

HOST = "127.0.0.1"
PORT = 5000


def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Lista de actividades disponibles
    actividades = {
        "1": "Registrar usuario",
        "2": "Consultar información",
        "3": "Actualizar registro",
        "4": "Eliminar registro",
        "5": "Generar reporte"
    }

    try:
        cliente.connect((HOST, PORT))

        archivo = cliente.makefile("r", encoding="utf-8")

        print("\n========================================")
        print("       ¡Bienvenido al Store Market!")
        print("========================================")

        while True:
            print("\nIngresa el numero de la actividad que desea realizar:\n")
            print("1. Registrar usuario")
            print("2. Consultar información")
            print("3. Actualizar registro")
            print("4. Eliminar registro")
            print("5. Generar reporte")
            print("6. Salir")

            opcion = input("\nSelecciona una opción: ").strip()

            # Opción para salir
            if opcion == "6":
                print("\n¡Gracias por utilizar nuestro servicio!")
                print("¡Espero verte pronto!")
                break

            # Validar opción ingresada
            if opcion not in actividades:
                print("\nOpción inválida. Por favor, selecciona un número del 1 al 6.")
                continue

            tarea = actividades[opcion]

            # Preparar los datos en formato JSON
            datos = {
                "tarea": tarea
            }

            mensaje = json.dumps(datos) + "\n"

            # Enviar tarea al servidor
            cliente.sendall(mensaje.encode("utf-8"))

            print(f"\n[CLIENTE] Actividad seleccionada: {tarea}")
            print("[CLIENTE] Tarea enviada. Esperando resultado...")

            # Recibir respuesta del servidor
            respuesta = archivo.readline()

            if not respuesta:
                print("[CLIENTE] El servidor cerró la conexión.")
                break

            resultado = json.loads(respuesta)

            print("\n========== RESULTADO ==========")
            print("Worker:", resultado["worker"])
            print("Tarea:", resultado["tarea"])
            print("Respuesta:", resultado["resultado"])
            print("================================")

        archivo.close()

    except ConnectionRefusedError:
        print("[CLIENTE] No se pudo conectar con el servidor.")

    except (ConnectionError, OSError, json.JSONDecodeError) as error:
        print("[CLIENTE] Error:", error)

    finally:
        cliente.close()
        print("[CLIENTE] Conexión finalizada.")


if __name__ == "__main__":
    iniciar_cliente()
