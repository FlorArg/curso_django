# Vistas

.fx: title

---

# Vistas
Basicamente una vista o view es un "tipo" de página web en nuestra aplicación, 
generalmente provee una función específica. Generalmente tiene una plantilla
asociada.

En su forma mas simple una view es una funcion en Python que recibe el
**request** como parametro y luego de realizar alguna tarea genera y retorna un 
objeto **response**.

    !python
    
    from django.http import HttpResponse

    def index(request, nombre):
        return HttpResponse("Hola %s." % nombre)

> Como se ejecuta la vista?

---

# Mapeo de URLs

En Django el contenido se entrega a partir de views, y el encargado de determinar
qué view se ejecuta es un módulo Python informalmente llamado *URLconfs*.

Estos módulos definen como se mapean las URL (expresiones regulares) a funciones
(las views).

    !bash
    mysite/
        myapp/
            __init__.py
            models.py
            views.py
            urls.py  <--- Agregamos

En url.py argeamos la tupla que mapea la url en nuestra view
            
    !python
    
    from django.conf.urls import patterns, url
    
    from myapp import views
    
    urlpatterns = patterns('',
        url(r'^(\w+)$', views.index, name='index')
    )


# Class Views

