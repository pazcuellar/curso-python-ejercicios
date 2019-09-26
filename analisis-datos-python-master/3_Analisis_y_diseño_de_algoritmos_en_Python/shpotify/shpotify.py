from os import system
def clear_console():
    system('clear')

#inicializar lista global de biblioteca
biblioteca_musica = []

def crear_diccionario_de_cancion(str_cancion):
    #str_cancion = ID|artista|cancion|duracion|link a youtube
    valores_partidos = str_cancion.split('|')

    #valores_partidos = [ID, artista, cancion, duracion, link]
    return {
        "id":valores_partidos[0],
        "artista":valores_partidos[1],
        "nombre_cancion":valores_partidos[2],
        "duracion":valores_partidos[3],
        "link":valores_partidos[4]
    }

#Función que lee el archivo de texto que contiene la biblioteca
#y crea la lista del diccionario de canciones
def leer_biblioteca():
    archivo_de_biblioteca = open('biblioteca.txt', 'r')
    for linea_cancion in archivo_de_biblioteca:
        diccionario = crear_diccionario_de_cancion(linea_cancion.strip())
        biblioteca_musica.append(diccionario)

def mostrar_biblioteca():
    clear_console()
    print("----------Biblioteca----------")
    for cancion in biblioteca_musica:
        print("[{}] {}".format(cancion['id'], cancion['nombre_cancion']))
    print("-------------------------------")
    input("presiona cualquier tecla para continuar")

def mostrar_menu_y_capturar_opcion():
    clear_console()
    print("----------Menú----------")
    print("1. Ver biblioteca")
    print("2. Ver detalle por ID")
    print("3. Agregar canción")
    print("4. Eliminar canción")
    print("5. Terminar")
    print("-"*25)
    opc = input("opción: ")
    return opc

def mostrar_detalle_de_cancion():
    id = input("Id de la canción: ")
    cancion_por_mostrar = None
    for cancion in biblioteca_musica:
        if id == cancion['id']:
            cancion_por_mostrar = cancion
    if cancion_por_mostrar == None: #quiere decir que no existe la canción
        print("Ese ID no existe")
    else:
        print("---------------------------------")
        print("{} - {} ({})".format(cancion_por_mostrar['nombre_cancion'], cancion_por_mostrar['artista'], cancion_por_mostrar['duracion']))
        print("Escucha ahora:", cancion_por_mostrar['link'])
        print("---------------------------------")
    input("presiona cualquier tecla para continuar")
 

def crear_nueva_cancion():
    clear_console()
    nuevo_id = input("ID de la canción: ")
    id_existe = False
    for cancion in biblioteca_musica:
        if nuevo_id == cancion['id']:
            id_existe = True
    if id_existe == True:
        print("El ID existe.")
        input("Presiona cualquier tecla para continuar")
    else:
        nombre_cancion = input("Nombre: ")
        artista = input("Artista: ")
        duracion = input("Duración: ")
        link = input("Link a youtube: ")
        nueva_cancion = {
            "id": nuevo_id,
            "nombre_cancion": nombre_cancion,
            "artista": artista,
            "duracion": duracion,
            "link" : link
        }
        biblioteca_musica.append(nueva_cancion)
        print("Tu canción se creó con éxito")
        input("Presiona cualquier tecla para continuar")

def eliminar_cancion():
    clear_console()
    nuevo_id = input("ID de la canción: ")
    cancion_por_eliminar = None
    for cancion in biblioteca_musica:
        if nuevo_id == cancion['id']:
            cancion_por_eliminar = cancion
    if cancion_por_eliminar == None:
        print("")
        print("El ID no existe.")
        input("Presiona cualquier tecla para continuar")
    else:
        biblioteca_musica.remove(cancion_por_eliminar)
        print("La canción se eliminó con éxito")
        input("Presiona cualquier tecla para continuar")

def guardar_cambios():
    archivo_de_texto = open('biblioteca.txt', 'w')
    for cancion in biblioteca_musica:
        cancion_str = "{}|{}|{}|{}|{}".format(cancion['id'], cancion['artista'], cancion['nombre_cancion'], cancion['duracion'], cancion['link'])
        archivo_de_texto.write(cancion_str)
        archivo_de_texto.write("\n")
    print("Los cambios se guardaron con éxito.")

#1. Cargar la biblioteca al programa
leer_biblioteca()
opcion_elegida = ""
while opcion_elegida != "5":
    opcion_elegida = mostrar_menu_y_capturar_opcion()
    if opcion_elegida == "1":
        mostrar_biblioteca()
    elif opcion_elegida == "2":
        mostrar_detalle_de_cancion()
    elif opcion_elegida == "3":
        crear_nueva_cancion()
    elif opcion_elegida == "4":
        eliminar_cancion()
    elif opcion_elegida == "5":
        guardar_cambios()