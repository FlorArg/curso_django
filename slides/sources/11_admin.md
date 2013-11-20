
# Admin Site

    !python
    
    INSTALLED_APPS ( ... 
    'django.contrib.admin', )

Creamos un sitio de administración
common/admin.py

    !python
    
    from django.contrib import admin
    
    mascotas = admin.AdminSite("mascotas")

Agregamos las urls del sitio a URLconfs
myproject/urls.py

    !python
    from common.admin import mascotas

    urlpatterns = patterns('',
        (r'^mascotas/', include(mascotas.urls)),
    )

---

# Modelos

    !python
    
    mascotas.register(Persona)
    mascotas.register(Mascota)
    mascotas.register(Especie)
    mascotas.register(Raza)

---

# Inlines

    !python
    class MascotaInline(admin.TabularInline):
        model = Mascota
    
    class PersonaAdmin(admin.ModelAdmin):
        inlines = ( MascotaInline, )
