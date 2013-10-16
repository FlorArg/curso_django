# Aplicaciones de terceros

.fx: title

---

# Por que utilizar aplicaciones de 3ros

Si bien django provee un buen numero de características como

* ORM
* Sesiones, autenticación y autorización
* Gestión de email
* Mensajes
* GIS
* Administración automática

disponemos de muchos paquetes de 3ros que se instalan con **pip** y
proveen extensiones, comandos, template tags, vistas genericas, etc.


---


<img src="images/3ros.gif" style="padding-top: 20%">

<p style="text-align: center;">

Las aplicaciones de terceros ahorran mucho tiempo.
</p>

---

# South

---

# Que hace?

Permite manejar versiones de base de datos. Faclita el desarrollo iterativo incremental,
permitiendo aumentar minimizar el uso de SQL al momento de modificar los modelos.

Provee comandos de **manage.py** para:

1. Analiza las diferencias entre models.py y la base de datos
   y genera un script de migración

2. Aplica o desaplica migraciones de esquema (estructura)

3. Convierte aplicaciones que no usen South, en aplicaciones con South

4. Aplica o desaplica migraciones de datos (estructura)

2 y 4 son transparentes


---

# Instalación y uso

Se instala con pip en nuestro ambiente

    !bash

    pip install South

Se agrega como una aplicación instalada en setting.py en la lista de **INSTALLED_APPS**.

    !python

    INSTALLED_APPS = (
        ...
        'south',
    )


---

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

---


