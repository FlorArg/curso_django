# Plantillas

Las plantillas o templates son la forma que provee Django para separar el
diseño del código Python.

Directorio de plantillas

    !bash
    mysite/
        ...
        mysite/
        templates/      <---- Ruta para los templates
            myapp/      <---- Buenas practicas

En el modulo de settings.

    !python
    TEMPLATE_DIRS = (
        'templates',
    )

---

# Usando plantillas

Creamos un template en **templates/myapp/index.html**

    !html
    {% if modelos %}
        <ul>
        {% for modelo in modelos %}
            <li>{{ modelo }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>Sin datos.</p>
    {% endif %}

Modificamos la vista *index* en **myapp/views.py**

    !python
    from django.http import HttpResponse
    from django.template import Context, loader
    from myapp.models import Modelo
    from django.shortcuts import render_to_response

    def index(request):
        context = {'modelos': Modelo.objects.all()}
        return render_to_response('myapp/index.html', context)
---

# Herencia esqueleto

Una de las partes mas poderosas del motro de plantillas es la herencia.

El mecanismo consiste en definir una base o esqueleto de plantilla y mediante la
herencia redefinir bloques o partes de ese esqueleto.

    !html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <link rel="stylesheet" href="style.css" />
        <title>{% block title %}Mi sitio{% endblock %}</title>
    </head>
    <body>
        <div id="sidebar">
            {% block sidebar %}
            <ul>
                <li><a href="/">Inicio</a></li>
            </ul>
            {% endblock %}
        </div>
        <div id="content">
            {% block content %}{% endblock %}
        </div>
    </body>
    </html>

---

# Herencia redefinir

    !html
    {% extends "base.html" %}

    {% block title %}Mi super sitio{% endblock %}

    {% block content %}
    {% for modelo in modelos %}
        <h2>{{ modelo.titulo }}</h2>
        <p>{{ modelo.contenido }}</p>
    {% endfor %}
    {% endblock %}

