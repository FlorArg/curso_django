# Django<blockquote><p>The Web framework for perfectionists with deadlines</p></blockquote>

.fx: title

---

# Que es una framework

Un programador utilizar generalmente librerías que están
incluidas en su lenguaje y muchas veces librerías de
externos que proveen funcionalidad adicional a su porgrama.

Un framework brinda el *programa* y tiene un comportamiento
definido que el programdor modifica para adaptarlo a sus
necesidades.

![framework](images/architecture-framework-libraries.png)

---

# Estructura

![estructura](images/django_architecture.png)

---
# Proyecto

* Un desarrollo es un Proyecto
* Un proyecto puede hacer funcionar varios sitios web
* Un proyecto consta de una o mas aplicaciones

## Crear un proyecto

    !bash
    django-admin.py startproject mysite

## Estructura

    !bash
    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py

---

# Servidor de desarrollo

    !bash
    python manage.py runserver

## Abrimos http://localhost:8000

![runserver](images/runserver.png)