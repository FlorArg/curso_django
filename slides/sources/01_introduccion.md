# Introducción al desarrollo de aplicaciones web

.fx: home

# Presenter Notes

Arrancamos

----

# Bienvenidos

Defossé Nahuel, van Haaster Diego Marcos

----

# Python

.fx: bigbullet

* Interpretado
* Multiparadigma
* Tipado dinámico
* Interactivo

---

# Python - Sintaxis

Los bloques de código están definidos mediante la indentación. No se usan las { ... }.

    !python
    class Django(object):
        def do_my_webapp(self):
            print("develop, develop, develop")
    
    if __name__ == "__main__":
        dj = Django()
        dj.do_my_webapp()
        
---

# Python - Tipos de datos

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

# Django

.fx: centerquote

> The Web framework for perfectionists with deadlines