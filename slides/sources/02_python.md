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
    class Django(object):
        def do_my_webapp(self):
            print("develop, develop, develop")
    
    if __name__ == "__main__":
        dj = Django()
        dj.do_my_webapp()
        
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
