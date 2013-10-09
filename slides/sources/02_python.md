# Python<blockquote><p>An interactive, object-oriented, extensible programming language</p></blockquote>

.fx: title

---

# Características

Se lo suele clasificar como:

* Interpretado
* Multiparadigma
* Tipado dinámico
* Interactivo

---

# Características

<dl>
    <dt>Legible</dt>
        <dd>Sintaxis intuitiva y estricta</dd>
    <dt>Productivo</dt>
        <dd>Necesitamos solo entre el 30 y el 50% de el código que necesitaríamos en C++, C# o Java.</dd>
    <dt>Portable</dt>
        <dd>Se ejecuta en Windows, Linux, MacOS, móviles y otras plataformas</dd>
    <dt>Extenso</dt>
        <dd><a href="http://docs.python.org/2.7/" target="_blank">Librería estandar </a>
            muy bien provista y gran cantidad de paquetes de terceros.</dd>
    <dt>Integrable</dt>

        <dd>Se puede integrar con C, C++, .Net, Java, SOAP, CORBA, etc.</dd>
</dl>

---

# Ejemplo

El hola mundo:

    !python

    print "Hola mundo"

Una función:

    !python

    def saludar(nombre="pepe"):
        return "Hola %s" % nombre

Una clase

    !python

    class Animal(object):
        def __init__(self, nombre):
            self.nombre = nombre

        def saludar(self):
            return "Hola! Soy %s" % self.nombre

---

# Ejemplo (cont)

Un for:

    !python

    # Iterar sobre cosas
    for s in ["casa", "pato", "pepe"]:
        print "El numero es: %s" % s

Otro for:

    !python
    numero = 4
    for i in range(10):
        print "%d x %d = %d" % (i, numero, numero*i)


---

# Sintaxis de objetos

Los bloques de código están definidos mediante la indentación. No se usan las { ... }.

    !python
    import sys

    class Django(Framework):
        def __init__(self, name):
            self.name = name
            print("Project %s created" % name)

        @classmethod
        def startproject(cls, name):
            return cls(name)

    class MySite(Django):
        def runserver(self):
            print("%s is running" % self.name)
            return 0

    def main(argv = sys.argv):
        mysite = MySite.startproject("mysite")
        return mysite.runserver()

    if __name__ == "__main__":
        sys.exit(main())

---

# Tipos de datos

    !python
    # Cadenas
    ref = "nombre"

    # Numeros
    num = 1

    # Tuplas
    ( 1, 2, ref )

    # Listas
    [ num, 2, "edad", True, False ]

    # Diccionarios
    { "nombre": "Pepe", "edad": 28 }

---

# Donde aprender más

Existen muchos recursos en linea donde aprender...

* Cursos Dicatados en años anteriores en la UNPSJB:

    * <a href="http://www.slideshare.net/nahueldefosse/clase-1-curso-introduccin-a-python-2012"
        target="_blank">Clase 1</a>
    * <a href="http://www.slideshare.net/nahueldefosse/clase-1-curso-introduccin-a-python-2012-15552018"
        target="_blank">Clase 2</a>
    * <a href="http://www.slideshare.net/nahueldefosse/slides03-15552028"
        target="_blank">Clase 3</a>
    * <a href="http://www.slideshare.net/nahueldefosse/slides04-15552032"
        target="_blank">Clase 4</a>

* <a href="python.org.ar" target="_blank">Python Argentina</a>
* <a href="http://python-no-muerde.googlecode.com/hg/python_no_muerde.pdf" target="_blank">
    Python no muerde, yo si</a>
* <a href="http://www.codecademy.com/tracks/python" target="_blank">
    Sección de Python de *Code Academy*</a>
* <a href="https://www.khanacademy.org/science/computer-science/" target="_blank">
    Sección de Python de *Kahn Academy*</a>
---

# Gestión de proyectos

---

## Paquetes de Python

Python tiene un gran número de paquetes disponibles más allá de los
que nos brinda la librería estandard y están disponibles en
<a href="http://pypi.python.org" target="_blank" title="También llamado CheeseShop">PyPi</a>

# Herramienta de Instalación

La herramienta pip (e *easy_install*) sirven para instalar paquetes

    !bash

    $ pip install django
    $ pip uninstall paquete
    $ pip search facebook

    $ pip install django-facebook-comments

# Instalación global

    !bash

    sudo pip install django


---

# Virtualenv


## Que resuelve?
Sin embargo **no es recomendable instalar paquetes de python en el sistema**.
Podemos pisar paquetes, o incluso tener conflictos con versiones de Python viejas.

## Que hace?
Virutalenv es un paquete que permite crear entornos virtuales, copiando la instalación
de python en una carpte oculta dentro del directorio del usuario (típicamente ~/.virtualenvs).

## Como se instala?
    !bash

    $ sudo pip install virtualenv virtualenvwrapper
    $ echo "source /usr/local/bin/virtualenvwrapper.sh" > ~/.basrc

Y cerramos la terminal.

---

# Virtualenv uso

## Crear un ambiente

    !bash

    nahuel@lubuntu:~$ mkvirtualenv mi_proyecto

    (mi_proyecto)nahuel@lubuntu:~$

# Activar un ambiente

    !bash
    nahuel@lubuntu:~$ workon mi_proyecto
    (mi_proyecto)nahuel@lubuntu:~$
    # Si hacemos which python nos da el del virtualenv

# Desactivar un ambiente

    !bash
    (mi_proyecto)nahuel@lubuntu:~$ deactivate
    nahuel@lubuntu:~$  # Si hacemos which python nos da el del sistema

# Paquetes del ambiente

    !bash
    (mi_proyecto)nahuel@lubuntu:~$ pip freeze # Listado de paquetes

---

# Virtualenv (cont)

## Volcado de paquetes instalados

    !bash
    pip freeze > requirements.txt

## Instalación de paquetes

    !bash
    pip install -r requirements.txt|

## Notas

*pip* funciona para paquetes que sean de código Python, pero existen paquetes que dependen
de librerías de C. Las versiones de pip más nueva tienen la capacidad de bajar binarios,
las versiones más viejas requieren la instalación de paquetes adicionales.