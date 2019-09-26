# Proyecto
## Shpotify
**Shpotify es una aplicación de consola permite al usuario gestionar su librería de música. ** 

Tu trabajo como líder de desarrollo es entregar un prototipo de shpotify en Python 3. Este prototipo debe realizar cuatro operaciones básicas:
1. Listar todas las canciones en la biblioteca
2. Ver información completa de una canción en específico
3. Agregar una nueva canción
4. Eliminar una canción

La biblioteca de canciones deberá estar almacenada en un archivo de texto con la siguiente estructura:

id|artista|cancion|duracion|link a youtube

**Nota: El id es un número entero que va a servir para que el usuario pueda seleccionar una canción a través de este id único. **

Ejemplo del archivo:

~~~~
1|Led Zeppelin|Stairwar to Heaven|8:05|https://www.youtube.com/watch?v=D9ioyEvdggk
2|Muse|Undisclosed Desires|3:56|https://www.youtube.com/watch?v=R8OOWcsFj0U
3|Green Day|Basket Case|3:02|https://www.youtube.com/watch?v=NUTGr5t3MoY|
~~~~

Ejemplo de ejecición del programa:

~~~~
Bievenido a Shpotify!

-----Menú de opciones-----
1. Ver biblioteca
2. Ver canción por ID
3. Crear canción
4. Eliminar canción por ID
5. Terminar
--------------------------
opción: 1

-----Biblioteca-----
[1] Stairwar to Heaven
[2] Undisclosed Desires
[3] Basket Case
--------------------

-----Menú de opciones-----
1. Ver biblioteca
2. Ver canción por ID
3. Crear canción
4. Eliminar canción por ID
5. Terminar
--------------------------
opción: 2

Id de la canción: 2
---------------------
Undisclosed Desires - Muse (3:56)
Escucha ahora: https://www.youtube.com/watch?v=R8OOWcsFj0U
---------------------


-----Menú de opciones-----
1. Ver biblioteca
2. Ver canción por ID
3. Crear canción
4. Eliminar canción por ID
5. Terminar
--------------------------
opción: 3

-----Crear canción-------
ID: 21
Artista: The Cranberries
Canción: Zombie
Duración: 5:01
Link: https://www.youtube.com/watch?v=R8OOWcsFj0U

Canción creada!
-------------------------


-----Menú de opciones-----
1. Ver biblioteca
2. Ver canción por ID
3. Crear canción
4. Eliminar canción por ID
5. Terminar
--------------------------
opción: 1

-----Biblioteca-----
[1] Stairwar to Heaven
[2] Undisclosed Desires
[3] Basket Case
[21] Zombie
--------------------


-----Menú de opciones-----
1. Ver biblioteca
2. Ver canción por ID
3. Crear canción
4. Eliminar canción por ID
5. Terminar
--------------------------
opción: 4

ID de la canción por eliminar: 2
Canción 'Undisclosed Desires' eliminada


-----Menú de opciones-----
1. Ver biblioteca
2. Ver canción por ID
3. Crear canción
4. Eliminar canción por ID
5. Terminar
--------------------------
opción: 5
Bye!
Los cambios a tu biblioteca se guardaron con éxito.
~~~~

Como lo muestra la ejecución del programa, todo cambio que se le haga a la biblioteca de música tendrá que guardarse en el archivo de texto que almacena la información de la biblioteca.


La estructura de tu carpeta debería ser la siguiente:

- repositorio
    - shpotify
        - shpotify.py
        - biblioteca.txt

