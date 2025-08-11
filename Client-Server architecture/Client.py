import socket
from test import verificar_letras, verificar_usuario, verificar_longitud

FORMATO = 'utf-8'

def mostrar_menu():
    print("### ----------- Menú de Usuario ---------- ###")
    print("1. Generar nombre de usuario")
    print("2. Generar dirección de correo electrónico")
    print("0. Salir")

def main():
    HOST = '127.0.0.1'  # Cambiar por la IP del servidor si está en otra máquina
    PORT = 65432            # Puerto en el que está escuchando el servidor

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            info_usuario = {"usuario":"","correo":""}

            while True:
                mostrar_menu()

                opcion = input("Elija una opcion: ")

                if opcion == '1':
                    longitud = int(input("[CLIENTE PY] Ahora elija una longitud: "))

                    if(verificar_longitud(longitud)):
                        mensaje = f"{opcion}:{longitud}"

                        s.sendall(mensaje.encode(FORMATO))
                    
                    # Espero la respuesta del usuario generado
                        respuesta = s.recv(1024).decode()

                    # Se inicializa la variable "usuario", por lo que ya no es None
                        info_usuario["usuario"] = respuesta

                # La muestro por pantalla
                        print(f"[CLIENTE PY]: Usuario generado {respuesta}")
                    else:
                        print("[CLIENTE PY][ERROR]: La longitud no es valida")
                    
                elif opcion == '2':
        # En caso de que el cliente no haya generado un usuario con la opcion 1
                    if info_usuario["usuario"] == "":
                        info_usuario["usuario"] = input("[CLIENTE PY]: Ingrese un nombre de usuario: ")

                    if verificar_usuario(info_usuario["usuario"]):
                        mensaje = f"{opcion}:{info_usuario['usuario']}"
                        s.sendall(mensaje.encode(FORMATO))

                    # Espero una respuesta
                        respuesta = s.recv(1024).decode()
                    # La muestro por pantalla
                        print(f"[CLIENTE PY]: Correo generado {respuesta}")
                    
                    else:
                        print("[CLIENTE PY][ERROR]: El nombre de usuario no cumple con alguno de los siguientes requisitos:\n1. Debe contener al menos una consonante y una vocal\n2. Debe tener una longitud entre 5 y 20 caracteres\n3. No debe contener números")

                elif opcion == '0':
                    print("[CLIENTE PY]: Se ha desconectado")
                    break

                else: 
                    print("[CLIENTE PY][ERROR]: Opcion invalida")

    except ConnectionRefusedError:
        print("No se pudo conectar con el servidor.")

    except Exception as e:
        print(f"### [CLIENTE PY][ERROR]: {e} ###")

main()