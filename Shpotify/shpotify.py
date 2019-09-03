f = open('biblioteca.txt')
canciones = []
for linea in f:
    cancion = {}
    valores = linea.strip().split('|')
    cancion = {
        "id": valores[0],
        "artista": valores[1],
        "cancion": valores[2],
        "duracion": valores[3],
        "link": valores[4],
    }
    canciones.append(cancion)
f.close()

print(len(canciones))

def ver_biblioteca(cancion):
    print("*"*20)
    print("ID: ", cancion['id'])
    print("artista: ", cancion['artista'])
    print("nombre de canción: ", cancion['cancion'])
    print("duración: ", cancion['duracion'])
    print("Escuchar ahora: ", cancion['link'])
    print("*"*20)

def ver_cancion_ID(cancion):
    print("*"*20)
    print("ID: ", cancion['id'])
    print("artista: ", cancion['artista'])
    print("nombre de canción: ", cancion['cancion'])
    print("duración: ", cancion['duracion'])
    print("Escuchar ahora: ", cancion['link'])
    print("*"*20)

##porque imprime 2 veces la cancion que se agrega, en el ultimo elemento existente 
## y en uno nuevo

def crear_cancion(ID, canciones):
    cancion['id'] = ID
    cancion['artista'] = input("nombre del artista: ")
    cancion['cancion'] = input("nombre de la canción: ")
    cancion['duracion'] = input("duración de la canción: ")
    cancion['link'] = input("link de YouTube: ")
    canciones.append(cancion)

##porque marca error cuando vuelvo a elegir la opción 1 
## después de eliminar una canción con la opción 4?

def eliminar_cancion(cancion):
    del cancion['id']
    del cancion['artista']
    del cancion['cancion']
    del cancion['duracion']
    del cancion['link']
    print("Canción eliminada")

def mostrar_menu():
    print("{}Menú{}".format("*"*10, "*"*10))
    print("1. Ver biblioteca")
    print("2. Ver canción por ID")
    print("3. Crear canción")
    print("4. Eliminar canción por ID")
    print("5. TERMINAR")
    print("*"*25)
    opc = input("Opción: ")
    return opc

opcion_elegida = "0"
while opcion_elegida != "5":
    opcion_elegida = mostrar_menu( )
    if opcion_elegida == "1":
        for cancion in canciones:
            ver_biblioteca(cancion)
    elif opcion_elegida == "2":
     Ocancion = input("ID de la canción: ")
     for cancion in canciones:
         if Ocancion == cancion['id']:
             ver_cancion_ID(cancion)   
    elif opcion_elegida == "3":
        NewID = len(canciones)+1
        Ncancion = len(canciones)-1
        crear_cancion(NewID, canciones)
    elif opcion_elegida == "4":
          Ecancion = input("ID de la canción: ")
          for cancion in canciones:
              if Ecancion == cancion['id']:
                  eliminar_cancion(cancion) 

print ("Bye Bye")






