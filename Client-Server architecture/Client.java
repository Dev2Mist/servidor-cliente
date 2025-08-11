import java.io.*;
import java.net.*;
import java.util.Random;
import java.util.Scanner;

public class Client {
    
    static final String HOST = "192.168.0.254";  // IP del servidor
    static final int PUERTO = 65432;             // Puerto del servidor

    static Random random = new Random();
    static Scanner scanner = new Scanner(System.in);

    public static void mostrarMenu() {
        System.out.println("### ----------- Menú de Usuario ---------- ###");
        System.out.println("1. Generar nombre de usuario");
        System.out.println("2. Generar dirección de correo electrónico");
        System.out.println("0. Salir");
    }

    public static boolean verificarLongitud(int longitud) {
        if (longitud < 5 || longitud > 20) {
            return false;
        } else {
            return true;
        }
    }

    public static boolean verificarUsuario(String usuario) {
        return usuario.matches(".*[aeiouAEIOU].*") &&
                usuario.matches(".*[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ].*") &&
                usuario.length() >= 5 &&
                usuario.length() <= 20 &&
                !usuario.matches(".*\\d.*");
    }

    public static void main(String[] args) {
        
        try (
            Socket socket = new Socket(HOST, PUERTO);
            BufferedReader lector = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            BufferedWriter escritor = new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()))
            ) {
            
            String usuarioGenerado = "";
            
            while (true) {
                mostrarMenu();
                System.out.print("Elija una opción: ");
                String opcion = scanner.nextLine();

                if (opcion.equals("1")) {
                    System.out.print("[CLIENTE JAVA]: Ingrese una longitud: ");
                    int longitud;

                    longitud = Integer.parseInt(scanner.nextLine());
                    
                    if (verificarLongitud(longitud) == true) {
                        String mensaje = opcion + ":" + longitud;

                        escritor.write(mensaje);
                        escritor.newLine();
                        escritor.flush();
                        
                        String respuesta = lector.readLine();

                        usuarioGenerado = respuesta;

                        System.out.println("[CLIENTE JAVA]: Usuario generado " + respuesta);
                    } else {
                        System.out.println("[CLIENTE JAVA][ERROR]: La longitud no es válida");
                    }

                } else if (opcion.equals("2")) {
                    if (usuarioGenerado.isEmpty()) {
                        System.out.print("[CLIENTE JAVA] Ingrese un nombre de usuario: ");
                        usuarioGenerado = scanner.nextLine();
                    }

                    if (verificarUsuario(usuarioGenerado)) {
                        String mensaje = opcion + ":" + usuarioGenerado;
                        escritor.write(mensaje);
                        escritor.newLine();
                        escritor.flush();
                        
                        String respuesta = lector.readLine();
                        System.out.println("RESPUESTA DEL SERVIDOR: " + respuesta);
    
                        System.out.println("[CLIENTE JAVA]: Correo generado: " + respuesta);
                    } else {
                        System.out.println("[CLIENTE JAVA][ERROR]: El nombre de usuario no cumple con alguno de los requisitos:");
                        System.out.println("[CLIENTE JAVA][ERROR]: 1. Al menos una vocal y una consonante");
                        System.out.println("[CLIENTE JAVA][ERROR]: 2. Longitud entre 5 y 20 caracteres");
                        System.out.println("[CLIENTE JAVA][ERROR]: 3. No debe contener números");
                    }

                } else if (opcion.equals("0")) {
                    System.out.println("[CLIENTE JAVA]: Se ha desconectado");
                    break;

                } else {
                    System.out.println("[CLIENTE JAVA][ERROR]: Opción inválida");
                }
            }

        } catch (IOException e) {
            System.out.println("[CLIENTE JAVA][ERROR]: No se pudo conectar al servidor.");
            System.out.println("[CLIENTE JAVA][ERROR]: " + e.getMessage());
        }
    }
}