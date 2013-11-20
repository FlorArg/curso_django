# Administración

---
# Estructura

La admin es un conjunto de vistas que permiten realizar CRUD de menera muy conveniente.

## La forma automágica

1) Activar la aplicación en el myproject/myproject/settings.py del proyecto

    !python
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',
        # Más cosas útiles
    )

---

2) Activar la URL en myproject/myproject/urls.py

    !python

    from django.conf.urls import patterns, include, url

    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        url(r'^$', 'asistencia.views.asistencia', name='home'),

        # Uncomment the next line to enable the admin:
        url(r'^admin/', include(admin.site.urls)),
    )
---

3) Crear un archivo admin.py en una aplicacion con:

    !python
    # myproject/common/admin.py
    from django.contrib import admin
    from django.db.models.loading import get_models

    for model in get_models():
        try:
            admin.site.register(model)
        except:
            pass

Una forma más controlada de *registrar* modelos en el
<a href="https://docs.djangoproject.com/en/dev/ref/contrib/admin/"
target="_blank">sitio de *administración*</a>.

    !python
    # myproject/common/admin.py
    from django.contrib import admin
    from common import models

    admin.site.register(models.Mascota)
    admin.site.register(models.Persona)




---
# Modificando los templates

La administración está distribuida en varios templates:

# Listado de aplicaciones

    admin/base.html
    admin/base_site.html
    admin/index.html

# Listado de objetos

    admin/base.html
    admin/base_site.html
    admin/change_list.html

# Formulario de alta/modificacion

    admin/base.html
    admin/base_site.html
    admin/change_form.html
    admin/includes/fieldset.html

---
Estos templates se pueden modificar globalmente generando la misma estrcutrua, o
defineindolos específicamente para el sitio:

    !python

    from django.contrib import admin

    class MiSitioAdministrativo(admin.AdminSite):
         index_template = None
        app_index_template = None

Recordar que se puede investigar con la consola interactiva:

    !bash
    (myproject) $ python manage.py shell

    In [0]: from django.contrib import admin

    In [1]: admin.AdminSite??


---

# Modificando las columnas

Para modificar columnas, es necesario registrar el modelo
con una clase de ModelAdmin dónde se indican opciones:

    !python
    # myproject/common/admin.py

    from django.contrib import admin

    class MascotaAdmin(admin.ModelAdmin):
        list_display = ('nombre', 'sexo',)



---

# Columnas personalizadas

---

# Ordenamiento de columnas personazliadas

---

# Filtrando por atributos relacionados


---
# Filtrando resultados


---
# Acciones

---
# Urls personalizadas

---
# Inlines