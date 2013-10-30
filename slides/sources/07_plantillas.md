# Plantillas

Las plantillas o templates son la forma que provee Django para separar el
diseño del código Python.

Agregamos un directorio para los templates.

    !bash
    mysite/
        manage.py
        myapp/
        mysite/
        templates/

En el modulo de settings.

    !python
    TEMPLATE_DIRS = (
        'templates',
    )

---

Herencia, inclusion
Template Tags
Filters
