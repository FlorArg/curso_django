# Aplicaciones de 3ros

.fx: title

---

# Por que utilizar aplicaciones de 3ros

Si bien django provee un buen número de características como

* <a href="https://docs.djangoproject.com/en/1.5/topics/db/models/">ORM</a>
* Sesiones, autenticación y autorización
* Gestión de email
* Mensajes
* <a href="http://bebblebrox.files.wordpress.com/2011/01/geodjango-pav-admin.png">GIS</a>
* <a href="http://django-dynamic-scraper.readthedocs.org/en/latest/_images/screenshot_django-admin_overview.png">Administración automática (y extensible)</a>

Disponemos de muchos paquetes de 3ros que se instalan con **pip** y
proveen extensiones, comandos, template tags, vistas genericas, etc.

---

<img src="images/3ros.gif" style="padding-top: 20%">

<p style="text-align: center;">
Las aplicaciones de terceros ahorran mucho tiempo.
</p>

---

# South

---

# Que es?

South es una herramienta de migración de datos, permite gestionar el cambio
en nuestros modelos desde un nivel de abstracción alto, minimizando de esta
manera el uso de SQL.

Agrega commandos en **manage.py** para trabajar dichos cambios:

1. Analiza las diferencias entre models.py y la base de datos y genera un
script de migración

2. Aplica o desaplica migraciones de esquema (estructura)

3. Convierte aplicaciones que no usen South, en aplicaciones con South

4. Aplica o desaplica migraciones de datos

2 y 4 son transparentes

---

# Instalación y Uso

Se instala con pip en nuestro ambiente

    !bash

    pip install South

Se agrega como una aplicación instalada en setting.py en la lista de **INSTALLED_APPS**.

    !python

    INSTALLED_APPS = ( 'south', )
    
Comandos basicos

    !bash

    # Convertir a South
    python manage.py convert_to_south common
    # Crear una migración
    python manage.py schemamigration common --auto
    # Aplicar una migración
    python manage.py migrate common
    # Listar
    python manage.py migrate common --list
    # Vovler a algún estado de la base de atos
    python manage.py migrate common 001

---

# Django Debug Toolbar

.fx: title

---

# Que es?

Es una coleccion de paneles configurables que presenta mucha informacion de debug
referida al request/response en curso.

## Que podemos ver dentro de toda esa informacion:

1. La vesion de Django
2. El tiempo de Request
3. Las configuraciones en settings.py
4. Los encabezados HTTP
5. Las variables de GET/POST/cookie/session
6. Las plantillas y los contextos usados para generar el HTML
7. Las consultas en SQL, sus tiempos y la explicacion de cada una
8. Las señales emitidas
9. Los logs emitidos por el modulo de logging configurado en Django

---

# Instalación

Instalacion con pip

    !bash

    pip install django-debug-toolbar

Modificamos settings.py para agregar la aplicacion, el middleware y algo de seguridad.

    !python

    INSTALLED_APPS = (
        ...
        'debug_toolbar',
    )

    # El orden es imporatante, debe estar despues de los middlewares que apliquen algun encoding sobre el response
    MIDDLEWARE_CLASSES = (
        # ...
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        # ...
    )
    
    # Solo para localhost
    INTERNAL_IPS = ('127.0.0.1',)

---

# Configuracion

En settings.py

    !python

    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
        'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
        'HIDE_DJANGO_SQL': False,
        'SHOW_TEMPLATE_CONTEXT': True,
        'TAG': 'div',
        'ENABLE_STACKTRACES' : True,
    }
