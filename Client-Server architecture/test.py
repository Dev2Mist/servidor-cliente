import random

DOMINIOS_VALIDOS = ["@gmail.com", "@hotmail.com"]
DOMINIOS_NO_VALIDOS = ["@yahoo.com","@outlook.com","@mail.com"]
VOCALES = ['a','e','i','o','u','A','E','I','O','U']
CONSONANTES = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
NUMEROS = ['1','2','3','4','5','6','7','8','9','0']

def verificar_longitud(longitud):
    if(longitud < 5 or longitud > 20):
        return False
    else:
        return True

def remover_saltos_linea(texto):
    return texto.replace('\n', ' ')

def hay_numeros(usuario):
    tiene_numero = any(letra in NUMEROS for letra in usuario)

    return tiene_numero

def verificar_letras(usuario):
    tiene_vocal = any(letra in VOCALES for letra in usuario)
    tiene_consonante = any(letra in CONSONANTES for letra in usuario)
    tiene_numeros = not hay_numeros(usuario)

    return tiene_vocal and tiene_consonante and tiene_numeros

def verificar_usuario(usuario):
    l = len(usuario)

    return verificar_longitud(l) and verificar_letras(usuario)

def generar_usuario_random(longitud):
# Verifico que la longitud ingresada es correcta
    if(verificar_longitud(longitud)):
        nombre = [random.choice(VOCALES), random.choice(CONSONANTES)]
        i = 0

        todas_letras = VOCALES + CONSONANTES

        while i < longitud-2:
            nombre += random.choice(todas_letras)
            
            i = i + 1
        return ''.join(nombre)

def generar_usuario():
    usuario = input("Ingrese su nombre de usuario: ")

    if(verificar_longitud(len(usuario)) and verificar_letras(usuario)):
        return usuario
    else:
        return

def generar_correo(nombre_usuario):
    if verificar_usuario(nombre_usuario):
        dominio = random.choice(DOMINIOS_VALIDOS)
        
        return f"{nombre_usuario}{dominio}"
    else:
        return