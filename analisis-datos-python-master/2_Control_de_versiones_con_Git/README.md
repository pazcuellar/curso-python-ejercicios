# Unidad II: Control de versiones con Git

## II.1. ¿Qué es Git?

Git es un sistema de control de versiones cuya función es *trackear* los cambios hechos al código fuente de programas computacionales. Git está diseñado para facilitar la coordinación entre programadores y equipos de programadores. Podemos pensar en Git como un Dropbox o Google Drive especial para código, en el cual no sólo almacenamos nuestros scripts sino que también llevamos una bitácora de todos los cambios que le hemos hecho a nuestro código a lo largo del tiempo. 


Git es utlizado tanto para proyectos de código abierto como cerrado. Su uso adecuado acelera significativamente el proceso de desarrollo de software. 


**Más información**
- [What is Git](https://www.atlassian.com/git/tutorials/what-is-git)


---

## II.2. ¿Qué es Github?
Github es la plataforma por excelencia para hostear repositorios de Git (proyectos de software). Es aquí en donde encontramos a la comunidad más proactiva y extensa del mundo del desarrollo de Software. Digamos que es la red social de todo programador.

[Exploremos Github](https://github.com)

Algunos proyectos hosteados en Github:
    - [Open Drop](https://github.com/seemoo-lab/opendrop)
    - [Chart.js](https://github.com/chartjs/Chart.js)
    - [Matplotlib](https://github.com/matplotlib/matplotlib)



---

## II.3. Tu cuenta de Github
Si aún no tienes una cuenta en Github, crea una en [este link](https://github.com/join)

---


## II.4. Github de este curso
Este curso cuenta con [un reposositorio público](https://github.com/nextia-academy/analisis-datos-python) en el cual podrán consultar las notas del curso, cuadernos de jupyter y otras ligas de interés.  


---

## II.5. Getting Started con Github

Lo primero que vamos a hacer es clonar un repositorio de Github. `Clonar` es el término correcto  que utlizamos en la jerga de Git para referirnos a la `descarga` de un repositorio a nuestra máquina. 

Existen muchas formas de hacer esto, sin embargo, este curso tiene como objetivo también sumergir a los estudiantes a un entorno  más afín a la ciencia computacional, y es por eso que durante este curso siempre vamos a promover el uso de la línea de comando sobre interfaces gráficas. 

Para este ejercicio, trabajeremos con el repositorio público [repo-de-prueba](https://github.com/nextia-academy/repo-de-prueba)

1. Abrir una terminal (MacOS, Linux) o Git Bash (Windows)
2. Es buena práctica tener una carpeta especial en nuestra máquina en donde almacenaremos nuestros proyectos/repositorios de código. Una buena opción puede ser `~/code`
3. En tu terminal, ejecuta los siguientes comandos
    ```
    cd
    mkdir code
    cd code
    ```
4. Mostrar la ayuda de git
    ```
    git help
    ```
5. Clonar el repositorio
Existen dos formas, o mejor dicho, protocolos, para clonar un repositorio a través de la línea de comando: https y ssh.  El más sencillo de éstps, el cual veremos hoy, es el protocolo HTTPS.
    ```
    git clone https://github.com/nextia-academy/repo-de-prueba
    ```
6. Ahora tenemos un directorio llamado `repo-de-prueba` en la carpeta que elegimos en el punto 2. En este ejemplo, la ruta completa es `~/code/repo-de-prueba/`
7. Ingresamos a este directorio para ver los archivos del repositorio
    ```
    cd repo-de-prueba
    ```
---

## II.6. Trabajar en un repositorio

En este punto tenemos dos versiones del repositorio `repo-de-prueba`: Una versión local y una remota. El **repositorio local** es aquél que existe en nuestra máquina de desarrollo. Es aquí en donde concemtramos esfuerzos para cambiar código agregando funcionalidad, corrigiendo errores (o *bugs*), mejorando nuestros algoritmos, etc. Por otro lado, el **repositorio remoto** es aquél que está hospedado en nuestra plataforma de contorl de versiones (Github en este caso). Todos los archivos del repositorio remoto son visibles para todo el público (dependiendo de permisos) y contiene las últimas versiones del código.

Un flujo de trabajo - muy básico - con git es el siguiente:
1. Clonar un repositorio remoto
2. Hacer cambios al repositorio local
3. Describir mis cambios en un nuevo `commit` (piénsese en un commit como en un checkpoint).
4. Subir (`push` en jerga de Git) mis cambios al repositorio remoto para que sean de acceso público.

Pongamos esto en práctica con el repositorio de prueba.

1. Entramos al repositorio, y hacemos cambios a los archivos de código que deseemos modificar. 
2. Al terminar de modificar nuestros archivos, y estar seguros que éstos no contienen bugs, hacemos nuestro commit.
3. Hacer commit
    ```
    git commit main.py -m "Agregar comentarios"
    ```
4. Checamos el status del repo
    ```
    git status
    ```
5. Subimos nuestro commit
    ```
    git push
    ```
 
##### Tracked & Untracked files
Al trabajar en un repositorio, tenemos dos tipos de archivos: tracked files y untracked files.

- Tracked files: archivos que ya existían en el repositorio y por lo tanto el sistema de control de versiones git está llevando un registro continuo de todos los cambios que se le hagan a dicho archivo.
- Untracked files: todos los archivos de los cuales git no está enterado y por lo tanto no está monitoreando sus cambios. Cuando creamos un nuevo archivo en un repositorio, este archivo por defecto no está siendo monitoreado por git. Por lo tanto, para poder incluirlo en nuestro control de versiones, tenemos que especificarle a git que debe comenzar a hacerlo.

1. Creamos un nuevo archivo `calculadora.py` y agregamos una función de suma.
2. Checamos el estatus del repo
    ```
    git status
    ```
3. `calculadora.py` debe aparecer como archivo no monitoreado (untracked file). 
4. Especificamos a git que debe monitorearlo, o sea, lo **agregamos** a nuestro control de versiones
    ```
    git add calculadora.py
    ```
5. Checamos el estatus del repo
    ```
    git status
    ```    
6. Creamos un commit para este archivo
    ```
    git commit calculadora.py -m "agregar scripts de calculadora"
    ```
7. Subimos nuestros commits
    ```
    git push
    ```
 
---

## II.7. Actualizar mi repositorio local (git pull)
Habrá veces en las que alguien (o ustedes) hayan hecho cambios a un repositorio remoto y no tengan esta última versión en su repositorio local. La manera en la que actualizamos un repositorio local es *jalando* los últimos cambios del repositorio remoto al local. 

1. Ubicarse en el directorio del repositorio en cuestión.
2. Jalar los cambios
    ```
    git pull
    ```

---

## II.8. Actividad

1. Crea un repositorio público.
2. Clona el repositorio a tu computadora
3. Agrega archivos.
4. Sube los cambios a github
5. Comparte el url de tu repositorio con tu compañer@
6. Clona el repositorio de tu compañer@
7. Haz algunos cambios a **TU** repositorio y súbelos a **TU** repositorio
8. Jala los últimos cambios del repositorio de tu compañer@



---

## II.9. Overview de colaboración y pull requests
Leer acerca de pull requests en [esta liga](https://help.github.com/en/articles/about-pull-requests)


---

## II.10. Jupyter notebooks en github
Github y los cuadernos de Jupyter se llevan muy muy bien. Github incorporó la funcionalidad para que un Jupyter Notebook se despliegue en formato `markdown` (así como los archivos README.md). Esto permite que leamos un cuaderno en Github sin la necesidad de clonar el repositorio y sin la necesidad de ejecutar Jupyter.

[Aquí un cuaderno de muestra](una_muestra_de_jupyter_en_github.ipynb)


## Otros recursos
- [Cheat sheet](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)
- [Tutorial simple](https://rogerdudler.github.io/git-guide/)
- [Github](https://github.com)