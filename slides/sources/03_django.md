# Django<blockquote><p>The Web framework for perfectionists with deadlines</p></blockquote>

.fx: title

---

# Django

.fx: smallest

* Django es un framework web en Python de alto nivel que permite un desarrollo rápido y un diseño limpio y pragmático
* Django automatiza todo lo posible adhiriéndose al principio DRY (Don’t Repeat Yourself)
    * Pone énfasis en el re-uso, la conectividad y extensibilidad de componentes
    * Python es usado en todo del framework (archivos, configuraciones, modelos de datos)

## Notas Djangeras

Desarrollado para gestionar varias páginas orientadas a noticias de la World Company de Lawrence, Kansas<br />
En julio de 2005 fue liberado bajo la licencia BSD; y desde junio de 2008 la Django Software Foundation lleva adelante el proyecto<br />
Su nombre es en alusión al guitarrista de jazz gitano Django Reinhardt

## Quien usa Django o "notas cholulas"

Google AppEngine, Nasa, Bitbucket.org, Disqus, Instagram, ...

---

# Caracteristicas

* Mapeador de objectos Python a base de datos **ORM**

.notes: Definimos el modelo en Python y obtenemos una rica y dinamica API de acceso a datos

* Aplicaciones "enchufables"

.notes: Listas para usar admin, auth, session, localflavor

* Interfaz de administración automática

.notes: Save yourself the tedious work of creating interfaces for people to add and update content. Django does that automatically, and it's production-ready.

* Sistema de "vistas genéricas"

.notes: Crear, editar, elimniar entidades de la base, listados, paginadores

* Elegante diseño de URLs

.notes: Uso de expresiones regulares para despachar hacia las vistas.

* Sistema de plantillas basado en etiquetas

.notes: Basadas en HTML, con soporte de herencia, inclusion, condicionales, iteraciones.

* Sistema de Cache

.notes: Varios niveles y backends para cachear lo que se necesite de la forma mas flexible.

* Soporte de internacionalización

.notes: El framework ya viene con soporte a varios idiomas.

* Documentación incorporada

.notes: Accesible a través de la aplicación administrativa

---

# Un framework

Un programador utilizar generalmente librerías que están
incluidas en su lenguaje y muchas veces librerías de
externos que proveen funcionalidad adicional a su porgrama.

Un framework brinda el *programa* y tiene un comportamiento
definido que el programdor modifica para adaptarlo a sus
necesidades.

![framework](images/architecture-framework-libraries.png)

---

# Patron MTV

* Model → modelo de datos (models.py)
* View → vistas de datos (views.py)
* Template → plantillas de páginas (generalmente archivos HTML)

![estructura](images/django_architecture.png)

---
 
# Funcionamiento

.fx: bigbullets

* El usuario pide una URL (por GET ó POST)
* Django busca la primera URL que coincida con la solicitada (urls.py)
* Se ejecuta la vista (función) a la que apunta esa URL (views.py)
* En la vista se utilizan los models (modelos de datos) para consultar la BD
* Los datos resultantes se introducen en la plantilla (templates)
* Se devuleve una respuesta HTTP con el HTML generado

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

---

# Aplicación

* Dentro del proyecto utilizamos **manage.py** para crear aplicaciones

# Crear una app

    !bash
    python manage.py startapp myapp
    
## Estructura

    !bash
    mysite/
        manage.py
        myapp/
            __init__.py
            models.py
            views.py
            tests.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py

---

# Modelos

.fx: title

---

# Modelos

.fx: smallbullet

Los modelos encapsulan la información referente al dominio de la aplicacion web.
Compuestos por campos generalemnte cada modelo mapea a una unica tabla de la base de datos.

* Cada modelo es una clase en Python que hereda de django.db.models.Model.
* Cada atributo del modelo se corresponde con una columna en la base de datos.
* Con esto Django genera automaticamente una API de acceso a datos.

### Modelo

    !python
    from django.db import models
    
    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

### SQL

    !sql
    CREATE TABLE myapp_person (
        "id" serial NOT NULL PRIMARY KEY,
        "first_name" varchar(30) NOT NULL,
        "last_name" varchar(30) NOT NULL
    );

---

# Modelos - Campos

<div style="float: left; width:50%">
<h2>Básicos</h2>
<ul>
<li>BooleanField</li>
<li>CharField</li>
<li>TextField</li>
<li>IntegerField</li>
<li>FloatField</li>
<li>DateTimeField</li>
</ul>
<h2>Relaciones</h2>
<ul>
<li>ForeignKey</li>
<li>ManyToManyField</li>
<li>OneToOneField</li>
</ul>
</div>

<div style="float: right; width:50%">
<h2>Plus</h2>
<ul>
<li>EmailField</li>
<li>DateField</li>
<li>TimeField</li>
<li>SlugField</li>
<li>FileField</li>
<li>ImageField</li>
<li>CommaSeparatedIntegerField</li>
<li>IPAddressField</li>
<li>UrlField</li>
</ul>

</div>

---

# Consultas - QuerySets

algo

---

# Migración de modelos - South

algo

---

# Vistas

.fx: title

---

# Vistas
Class Views

---

# Mapeo de URLs

algo

---

# Plantillas
Herencia, inclusion
Template Tags
Filters

---

# Aplicación de terceras partes - django-extensions

algo

---

# Formularios

.fx: title

---

# Formularios
Fields
Widgets

---

# Validación
Diferentes usos del método clean

---

# Aplicaciones de terceros

.fx: title

---

# Aplicación de terceras partes - Crispy forms

algo

---

# Aplicaciones de terceras partes - Social Auth

algo

---

# Aplicaciones de terceras partes - Celery

algo

---

# Deployment

.fx: title

---

# Buenas prácticas y despliegue de una aplicación

algo

---

# Automatización de deployment y otras tareas mediante fabric.

algo

---

# Diversos esquemas de deployment (puesta en producción).

algo

---

# Integración de supervisor, gunicorn y Apache o Nginx.

algo
