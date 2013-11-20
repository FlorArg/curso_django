
# Medios estaticos

Se llaman medios estáticos a todos los archivos que Django *no* genera:

# Imagenes
# CSS
Establece el estilo del las páginas.

# JavaScript
Permite dar compoartamiento en el cliente como widgets, validaciones, AJAX, etc.

---

# Dónde se ubican

Los medios estáticos se configuran en el archivo settings.py

    !python

    # Archivos subidos por el usuario
    MEDIA_ROOT = 'static/media' # Debería ser una ruta absoluta
                                # (ver os.path)

    MEDIA_URL = '/static/media' #
    # URL para el resto de los archivos estático
    STATIC_URL = '/static/'
    # Archivos de la admin
    ADMIN_MEDIA_PREFIX = '/static/admin/'

    STATICFILES_DIRS = (
        'static'
    )
    # Donde se guardan los archivos en producción
    # (Ver collectstatic)
    STATIC_ROOT = 'static_files' # Esta se usa en producción

En producción revisar <a
target="_blank"
href="https://docs.djangoproject.com/en/1.5/howto/static-files/">
este link</a>.

---

# Uso de archivos estáticos en los templates

En los templates existe un templatetag que birnada el tag **static**.

    {% load staticfiles %}

    <img src="{% static "common/img.png" %}">

Esto nos independiza de la ubicación absoluta del archivo en el sistema de archivos.



---

# Estructura de templates

---

Los templates pueden ubicarse en el proyecto:

    myproject/
        common/
        reportes/
        templates/
            base.html     # <-- estructura general
            listados.html # <-- exitende a base

Y en las aplicaciones, los templates específicos
de la aplicaccion:

    myproject/
        common/
            urls.py
            views.py
            models.py
            templates/
                listado_mascotas.html
                alta_mascota.html
---

# Herencia de Templates

El template *padre* puede tener la seiguiente estrcutra

    !html
    <!-- myproject/templates/base.html -->
    {% load staticfiles %}
    <html>
        <head>
            <title>{{ title }}</title>
            {% static css/estilo.css %}
            {% block extrastyle %}
                <!-- Acá va el estilo -->
            {% endblock extrastyle %}
        </head>
        <body>
            {% block content %}
                <!-- Acá va el contenido -->
            {% endblock content %}
            {% block scripts %}
                <!-- Acá va el javascript -->
            {% endblock scripts %}
        </body>

    </html>

---

# Herencia de templates (cont)

Un template que hereda del ejemplo anterior

    !html
    <!-- myproject/common/templates/alta_mascota.html -->
    {% extends "base.html" %}

    {% block content %}
    <h1>Listado de Mascotas</h1>
    <table>
        <tr>
            <th>Nombre</th>
            <th>Dueño</th>
        </tr>
        {% for mascota in mascotas %}
        <tr>
            <td>{{ mascota.nombre }}</td>
            <td>{{ mascota.duenio }}</td>
        </tr>
        {% endfor %}
        <a href="{% url alta_mascota %}">
            Agregar Mascota
        </a>
    </table>
    {% endblock content %}


---

# Formularios

---

# Estructura de formularios

Un formulario es una clase que se encarga de:

    * Generar código HTML
    * Validar entrada

---


# Tipos de Formularios

Existen tres tipos de formularios:

## Los que heredan de django.forms.ModelForm
Permiten crear y modificar instancias del modelo que se
persiten en la base de datos. La validación se genera
a partir de la definición del modelo relacionado.

## Los que heredan de django.forms.Form
Se utlizan para generalmente para búsquedas.

## Los que heredan de django.forms.formsets
Son conjuntos de formularios. Se utilizan con o sin un formulario "fuerte".
Sirven para crear o editar muchos modelos del mismo tipo al mismo tiempo.

---

# Estructura de un formulario

## La clase form.Form
## Uno o más atributos forms.Field (ej: CharField, IntegerField)
Toman el nombre del atributo

## Por cada field existe un widget que puede ser modificado

    class MiForm(forms.Form):
        mi_campo = forms.CharField(widget=forms.widgets.TextInput)

Es responsable de la presentación en HTML

## Una clsae Meta

Permite agegar información, por ejemplo, en los ModelForm, el modelo asociado.

## Una clase Media

Permite definir JavaScript y CSS asociado al formulario. Al momento de pasrlo
al template, se hay que incluir  {{ form.media }}

---

## Estructura

Está consituido de menera muy similar a un modelo:

    !python

    from django import forms

    class BusquedaForm(forms.Form):
        nombre = forms.CharField()
        fecha = forms.DateField()

Generalmente se ubican en un módulo (archivo) a parte
de las vistas o las urls:

    common/          # <- directrio de la aplicación
        views.py
        urls.py
        forms.py     # <-- Acá!

---

# Uso


Y luego se importan en las vistas.

    !python

    # views.py

    from forms import BusquedaForm

    def mi_vista(request):
        """Esta vista utiliza un fomrulario"""
        if request.method == "GET":
            form = BusquedaForm()
            mascotas = Mascota.objects.none()
        else:
            form = BusquedaForm(request.POST)
            if form.is_valid():
                mi_campo = form.cleaned_data['mi_campo']
                mascotas = Mascota.objects.filter(nombre=mi_campo)
        return render_to_response("common/busqueda.html", {
            'form': form,
            'mascotas': mascotas
            })

---

# Template

    !html

    {% extends base.html %}

    {% block content %}
        <h1>Búsqueda</h1>
        <form action="GET">
            {% crsf_token %}
            {{ form }}
        </form>
        <h2>Resultados</h2>
        {% if mascotas %}
            <ul>
            {% for mascota in mascotas %}
                <li>{{ mascota.nombre }}</li>
            {% endfor %}
            </ul>
        {% else %}
            Sin resultados.
        {% endif %}

    {% endblock content%}

---

# Validación

La validación ocurre de la siguiente menra:

## Se llama al método clean de cada field
Validación básica del tipo de dato.

## Se llama al método clean_NOMBRE_FIELD si existe en el form

    !python
    class ContactForm(forms.Form):
        destinatarios = MultiEmailField()

        def clean_destinatarios(self):
            data = self.cleaned_data['destinatarios']
            if "pepe@example.com" not in data:
                raise forms.ValidationError("Te olvidaste de pepe!")
            # Siempre retornar data
            return data

---

# Validación (2)

## Se llama al método clean del form

    !python

    class ContactForm(forms.Form):
        asunto = forms.CharField(max_length=100)
        mensaje = forms.CharField()
        emisor = forms.EmailField()
        destinatario = MultiEmailField()
        con_copia = forms.BooleanField(required=False)

        def clean(self):
            cleaned_data = super(ContactForm, self).clean()
            con_copia = cleaned_data.get("con_copia")
            asunto = cleaned_data.get("asunto ")

            if con_copia and asunto:
                if "ayuda" not in asunto:
                    raise forms.ValidationError("No pidas 'ayuda' sin "
                            "incluirte con copia.")
            return cleaned_data


<a href="https://docs.djangoproject.com/en/1.5/ref/forms/validation/"
target="_blank">
    Documentación sobre validación en Django
</a>

---

# ModelForms

Los modelform utilizan la propiedad Meta para definir a que modelo referencia:

    !python

    from models import Mascota

    class MascotaForm(forms.ModelForm):

        class Meta:
            model = Mascota

Y tiene el método **save()** que genera una instancia del modelo.

    !python

    def alta_mascota(request):
        if request.moethod == 'GET':
            form = MascotaForm()
        else:
            form = MascotaForm(request.POST)
            if form.is_valid():
                form.save()
                # Todo OK :)
                return HttpResponeRedirect('..')
            return render_to_response('common/alta_mascota.html', {
                'form': form
                })

