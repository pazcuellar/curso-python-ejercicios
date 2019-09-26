#función para mostrar el menú de opciones y capturar la opción deseada
def mostrar_menu_y_capturar_opcion():
    print("*******************Menú******************")
    print("1. Encriptar mensaje")
    print("2. Desencriotar mensaje")
    print("3. Salir")
    print("*****************************************")
    return input("Opción: ")

#Función para encriptar un mensaje con un diccionario (alfabeto encriptado)
def encriptar_mensaje(mensaje, cipher):
    mensaje_encriptado = ''
    #por cada letra en el menesaje a encriptar
    for letra in mensaje:
        if letra == ' ':
            mensaje_encriptado += ' '
        else:
            #concatenamos el valor de la letra encriptada correspondiente
            mensaje_encriptado += cipher[letra]
    return mensaje_encriptado

#Función para desencriptar un mensaje encriptado
def desencriptar_mensaje(mensaje_encriptado):
    #obtenemos la llave secreta del usuario para asegurarnos de que es el receptor y no un ladrón de mensajes
    key = obtener_palabra_secreta()

    #obtenemos el diccionario encriptado
    #la función crear_diccionario(key) regresa una tupla de diccionarios.
    #sabemos que esta tupla tiene en la psición [0] el diccionario para encriptar
    #y en la posición [1] el diccionario para deseencriptar
    #por eso tenemos un [1] al final
    dicc_desenc = crear_diccionarios(key)[1]
    mensaje_desencriptado = ''
    for letra in mensaje_encriptado:
        if letra == ' ':
            mensaje_desencriptado += ' '
        else:
            mensaje_desencriptado += dicc_desenc[letra]
    return mensaje_desencriptado

#Función para crear ambos diccionarios: el que usamos para encriptar y el que usamos para desencriptar
def crear_diccionarios(key):
    alfabeto_real = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
    alfabeto_secreto = list(key)
    for letra in alfabeto_real:
        if letra not in alfabeto_secreto:
            alfabeto_secreto.append(letra)
    
    dicc_enc = {}
    dicc_desenc = {}
    indice = 0
    for letra in alfabeto_real:
        dicc_enc[letra] = alfabeto_secreto[indice]
        indice += 1
    
    for llave in dicc_enc:
        dicc_desenc[dicc_enc[llave]] = llave

    #este return regresa una tupla con el diccionario para encriptar en la posición [0] y el diccionario para desencriptar en la posición [1]
    return dicc_enc, dicc_desenc

#Función para crear key para encriptar
def obtener_palabra_secreta():
    #pedimos al usuario una palabra secreta o contraseña
    palabra_usuario = input("Palabra secreta: ")
    key = ''
    #creamos la llave eliminando las letras repetidas
    for letra in palabra_usuario:
        if letra not in key:
            key += letra
    return key.upper()

opcion = mostrar_menu_y_capturar_opcion()
if opcion == "1":
    key = obtener_palabra_secreta()
    dicc_encriptar, dicc_desencriptar = crear_diccionarios(key)
    mensaje = input("Mensaje: ").upper()
    mensaje_encriptado = encriptar_mensaje(mensaje, dicc_encriptar)
    print("Mensaje encriptado:", mensaje_encriptado)
elif opcion == "2":
    mensaje_encriptado = input("Mensaje encriptado: ")
    mensaje = desencriptar_mensaje(mensaje_encriptado)
    print(mensaje)
else:
    print("Adios!")