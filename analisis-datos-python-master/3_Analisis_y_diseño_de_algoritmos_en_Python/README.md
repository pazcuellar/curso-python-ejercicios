# Unidad III: Análisis y diseño de algoritmos en Python


## 1. Introducción a Python
[Python](https://python.org) es un lenguaje de programación orientado a objetos desarrollo a finales de la década de los 80s. En los últimos años, Python se ha vuelto sumamente popular, tanto así que ahora se considera la *lingua franca* de la ciencia de datos. Pueden leer más de Python en su página de [Wikipedia](https://es.wikipedia.org/wiki/Python).


Python es un languaje de intérprete. Esto quiere decir que los programas no se compilan a lenguaje de máquina. La ventaja de esto es que podemos correr, testear y debuggear nuestro código muy fácil y rápidamente.

Python es open-source y multiplataforma, lo cual significa que podemos correr un programa de python en cualquier sistema operativo.

Python es muy fácil de aprender y de enseñar. Gracias a su sintaxis simple - y concreta - podemos enfocarnos más en la lógica de nuestros programas que en aprender sintaxis y reglas tediosas.

---

A continuación se muestran el código en **`C#`** de un programa que pide al usuario su edad y éste determina si el usuario es mayor de edad o no. Posteriormente se muestar el mismo programa pero en código de **`Python`**

#### C#
```
using System;
namespace HolaMundo
{
    public static void Main(string[] args) 
    {
        Console.WriteLine("Hola Mundo!");

        //pedir edad
        Console.Write("Dame tu edad: ");

        //leer edad
        int edad = int.parse(Console.ReadLine());

        if (edad >= 18) 
        {
            Console.WriteLine("Eres mayor de edad.");
        }
        else 
        {
            Console.WriteLine("Eres menor de edad.");
        }
    }
}
```
#### Python
```
print("Hola mundo")
//pedir y leer edad
edad = int(input("Dame tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

---

## 2. Intérprete de Python
El intérprete de Python es el _compilador_ (está en cursivas porque no existe tal cosa como un compilador de Python) de Python. El intérprete es el encargado de ejecutar las líneas de código escritas en Python.

La forma más fácil de entrar al intérprete es a través de la línea de comando.

#### MacOS | Sistemas Unix | Windows
~~~~bash
python
~~~~
Algunos sistemas tienen python 2 instalado por defecto, y el comando `python` hace referencia a python2 en lugar de python3. En estos casos, el comando que queremos es
~~~~bash
python3
~~~~

La terminal entrará al intérprete de Python. Verán algo así:
	
~~~~shell
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
~~~~

En este intérpretete ya podemos escribir código de python.

~~~~python
>>> 5 + 5
10
>>> 5 * 9
45
>>> 45 / 7
6.428571428571429
>>> 45 / 5
9.0
>>> import math
>>> math.pi
3.141592653589793
>>> 9 ** 2
81
>>> 5 > 5
False
>>> 100 > 99
True
>>> 1 < 10
True
>>> 1 <= 1
True
>>> for i in [1,2,3,4,5,6]:
...     print(i)
... 
1
2
3
4
5
6
~~~~

El intérprete nos puede servir para ejecutar código rápidamente o hacer pruebas.

---

## 3. Archivos .py
Otra forma de ejecutar código de Python (y la más convencional) es escribiendo archivos de código con extensión `.py`. Veamos un ejemplo en consola. 
**Nota: esto no es necesario hacerlo en consola (ni tiene ninguna ventaja). Únicamente quiero mostrar el uso de terminal para que se vayan acostumbrando a ella.**

~~~~bash
pwd
/home/gemathus
~~~~
Estamos en el directorio `gemathus`. Vamos a crear un directorio especial para nuestro código. En bash, creamos directios con el comando `mkdir`, el cual es una abrevación de `make directory`

~~~~bash
mkdir code
cd code
pwd
/home/gemathus/code
~~~~

En este directorio vamos a crear otro directorio con el nombre `intro-a-python`
**Nota: es mala práctica ocupar espacios, acentos y caracteres especiales (que no sean el guión medio o bajo) en los nombres de archivos o directorios. El uso de mayúsculas ya depende de gusto personal. Yo prefiero siempre usar minúsculas para no tener que usar combinaciones de telcas (`shift + letra`) en la línea de comando para poder hacer todo más rápido.**
~~~~bash
mkdir intro-a-python
cd intro-a-python
~~~~

En este directorio vamos a crear un nuevo archivo de Python. El comando `touch` sirve para crear archivos

~~~~bash
touch mi_primer_archivo.py
~~~~

Este archivo lo podemos abrir con cualquier editor de texto:
- MacOS: TextEdit
- Sitemas UNIX: gedit
- Windows: Notepad (Bloc de notas)

Existen editores de texto de línea de comando muy populares. Uno de ellos es `vim`. Vim viene instalado por defecto en sistemas Unix, pero también se puede instalar en Windows y Mac.

[Tutorial básico de vim](https://www.howtoforge.com/vim-basics)

Abrimos nuestro archivo en el editor de texto de nuestra preferencia y agregamos la siguiente línea
~~~~python
print("Hola mundo!")
~~~~
Guardamos nuestro archivo y regresamos a la línea de comando. Para correr un archivo de pyhon desde línea de comando tenemos que llamar el comando python y pasar como primer argumento el archivo que queremos ejecutar.

```python3 [archivo.py]```

En este ejemplo:
~~~~bash
python3 mi_primer_archivo.py
Hola mundo!

~~~~

## 4. Python en un Jupyter Notebook
[Abrir Jupyter Notebook](1_Python_en_jupyter.ipynb)