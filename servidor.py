import socket
import threading
import queue
import json
import time

# Configuración del servidor
HOST = "127.0.0.1"
PORT = 5000

# Cola de tareas
cola_tareas = queue.Queue()

# Control de cierre
detener_workers = threading.Event()


# Worker que procesa las tareas
def worker(numero):
    print(f"[WORKER {numero}] Iniciado y esperando tareas...")

    while not detener_workers.is_set() or not cola_tareas.empty():
        try:
            tarea = cola_tareas.get(timeout=0.5)

        except queue.Empty:
            continue

        try:
            conexion = tarea["conexion"]
            descripcion = tarea["tarea"]
            bloqueo = tarea["bloqueo"]

            print(f"[WORKER {numero}] Procesando tarea: {descripcion}")

            # Simular procesamiento
            time.sleep(2)

            # Crear respuesta
            resultado = {
                "worker": numero,
                "tarea": descripcion,
                "resultado": f"Tarea '{descripcion}' procesada correctamente"
            }

            # Enviar respuesta al cliente
            mensaje = json.dumps(resultado) + "\n"

            with bloqueo:
                conexion.sendall(mensaje.encode("utf-8"))

            print(f"[WORKER {numero}] Tarea finalizada")

        except (ConnectionError, OSError) as error:
            print(f"[WORKER {numero}] Error de conexión: {error}")

        finally:
            cola_tareas.task_done()


# Crear los dos Workers
workers = []

for i in range(1, 3):
    hilo = threading.Thread(target=worker, args=(i,))
    hilo.start()
    workers.append(hilo)


# Recibir tareas de los clientes
def recibir_tareas(conexion, direccion):
    bloqueo = threading.Lock()

    with conexion:
        archivo = conexion.makefile("r", encoding="utf-8")

        for linea in archivo:
            try:
                datos = json.loads(linea)

                if "tarea" not in datos:
                    continue

                tarea = {
                    "tarea": datos["tarea"],
                    "conexion": conexion,
                    "bloqueo": bloqueo
                }

                cola_tareas.put(tarea)

                print(f"[SERVIDOR] Tarea recibida: {datos['tarea']}")

            except json.JSONDecodeError:
                print("[SERVIDOR] Mensaje inválido")


# Crear servidor TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

servidor.bind((HOST, PORT))
servidor.listen()

print(f"\n[SERVIDOR] Escuchando en {HOST}:{PORT}")
print("[SERVIDOR] Esperando conexiones...\n")


# Aceptar conexiones
try:
    while True:
        conexion, direccion = servidor.accept()

        print(f"\n[SERVIDOR] Cliente conectado: {direccion}")

        hilo_cliente = threading.Thread(
            target=recibir_tareas,
            args=(conexion, direccion)
        )

        hilo_cliente.start()

except KeyboardInterrupt:
    print("\n[SERVIDOR] Cerrando servidor...")

finally:
    servidor.close()
    detener_workers.set()

    for hilo in workers:
        hilo.join()

    print("[SERVIDOR] Servidor finalizado.")
