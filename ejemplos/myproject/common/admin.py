# encoding: utf-8

from django.contrib import admin
from django.db.models.loading import get_models
from models import *

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre',
                    'duenio',
                    'get_especie_domesticable'
                    )

    list_filter = ('nombre', 'duenio')

    def get_especie_domesticable(self, instancia):
        if instancia.especie.domesticable:
            return "Es <b>domesticable</b>"
        else:
            return "No es <i>domesticable</i>"
    get_especie_domesticable.short_description = "Domesticable"
    get_especie_domesticable.allow_tags = True


    fieldsets = (
        ("Información básica sobre su mascota", {
            'fields': (('nombre', 'duenio'), 'sexo')
            }
        ),
        ("Información complementaria", {
            'classes': ('collapse',),
            'fields': ('especie', )
            }
        ),
    )

admin.site.register(Mascota, MascotaAdmin)

class MascotaInline(admin.TabularInline):
    model = Mascota

class PersonaAdmin(admin.ModelAdmin):
    inlines = [MascotaInline, ]

admin.site.register(Persona, PersonaAdmin)

for model in get_models():
    try:
        admin.site.register(model)
    except:
        pass