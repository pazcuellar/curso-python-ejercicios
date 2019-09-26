# Unidad V: Exploración de datos con Pandas

El paquete pandas es la herramienta más importante para un analista de datos que trabaja con Python. Las librerías sofisticadas de machine learning o de visualización de datos se roban toda la atención, pero `pandas` es muchas veces el núcleo de los  proyectos.

El nombre `pandas` viene de *panel data*, un término de econometría que describe un conjunto de datos que contiene múltiples observaciones a lo largo de distintos periodos de tiempo para el mismo individuo.

`Pandas` es esencial para toda personsa que quiera embarcar en el campo de la ciencia de datos. 

### ¿Para qué es `pandas`?
En resumen, `pandas` será el nuevo hogar de tus datos. Pandas nos permite conocer nuestros datos, limpiarlos, transformarlos y analizarlos.

Supongamos que tenemos una base de datos en un archivo `.csv` de nuestra computadora. Con `pandas` podemos cargar este archivo a un `DataFrame` - una tabla - y realizar operaciones como las siguientes:
- Calcular estadísticos y contestar preguntas acerca de los datos:
    - Media, mediana, máximo, mínimo de cada columna
    - ¿Existe correlación entre la columna A y la B?
    - ¿Cómo se ve la distribución de la columna C?
- Limpiar datos con operaciones que eliminen valores faltantes
- Crear nuevas bases de datos a partir de filtros que cumplan con criterios que queramos fijar
- Visualizar datos con `matplotlib`
- Guardar los datos que transformamos a un nuevo archivo, o cargarlos a una base de datos relacional.

### ¿Cuándo puedo comenzar con `pandas`?
Pandas es un paquete que requiere que el analista tenga ćonocimientos sólidos de algorítmica y dell lenguaje Python. Más especificamente, el analista debe estar cómodo utilizando listas, tuplas, diccionarios, funciones y ciclos. También se recomienda que se haya trabajado con Numpy previamente.

### Instalación de `pandas`

~~~~bash
pip install --user pandas
~~~~

o

~~~~bash
pip3 install --user pandas
~~~~

o

~~~~bash
python -m pip install --user pandas
~~~~