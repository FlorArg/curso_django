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

    !python

    print "Hola mundo"


---

# Sintaxis

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

# Gestión de proyectos

Python tiene un gran número de paquetes disponibles más allá de los
que nos brinda la librería estandard.





