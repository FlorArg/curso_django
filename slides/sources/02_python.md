# Python<blockquote><p>An interactive, object-oriented, extensible programming language</p></blockquote>

.fx: title

---

# Caracteristicas

* Interpretado
* Multiparadigma
* Tipado dinámico
* Interactivo

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
