# Aplicaciones de 3ros

.fx: title

---

# Django extensions

---

# Que es?

---

# Instalación y Uso

Se instala con pip en nuestro ambiente

    !bash

    pip install django-extensions

Se agrega como una aplicación instalada en setting.py en la lista de **INSTALLED_APPS**.

    !python

    INSTALLED_APPS = ( 'django_extensions', )
    
Para ver los nuevos comandos disponibles

    !bash

    python manage.py help

Algunos comandos requieren la instalación de otras aplicaciones

* **export_emails**
    will require the python vobject module to create vcard files.
    
* **graph_models**
    requires pygraphviz to render directly to image file.
