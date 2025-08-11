import socket
import threading
from test import generar_usuario_random, generar_correo, remover_saltos_linea

FORMATO = 'utf-8'

def manejar_cliente(conn, addr):
    print(f"[+][SERVIDOR] Conectado con {addr}")
    
    with conn:
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break

                opcion, datos = data.split(":", 1)

                if opcion == "1":
                    respuesta = generar_usuario_random(int(datos))

                elif opcion == "2":
                    datos = datos.strip()
                    respuesta = generar_correo(datos)

                conn.sendall((respuesta+"\n").encode(FORMATO))                

            except Exception as e:
                conn.sendall(f"[SERVIDOR][ERROR]: {str(e)}".encode(FORMATO))
                break

    print(f"[-][SERVIDOR] Conexión cerrada con {addr}")

def main():
    HOST = '0.0.0.0'    # Acepta conexiones de cualquier IP
    PORT = 65432        # Puerto de escucha

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[SERVIDOR]: Escuchando conexiones con el puerto {PORT}...")

        while True:
            conn, addr = server.accept()
            hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
            hilo.start()

main()