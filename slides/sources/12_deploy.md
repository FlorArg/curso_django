# Deployment

La puesta en produccion de un proyecto Django suele contar
de las siguientes estapas:

1) Escritura del script de deployment

2) Ejecución del script de deployment

---

# Estructura típica


    Browser
     |
     +-+-+-+-+-
    ( internet )
     +-+-+-+-+-
     |
     *
    WebServer (Front End) ----------> Archivos estáticos
                          |           (STATIC_URL = '/static')
                          |
                          \.........> Application server (Todo lo demás)
                                  /       |
                                  |       |-> Worker #0 (Django 1)
                                  |       |-> ...
                                  |       \-> Worker #n (Django 2)
                                  |
    Supervisor ------------------/  (controla)
        - start
        - stop
        - restart

<a href="http://supervisord.org/">Supervisor</a>

<a href="http://gunicorn.org/">Gunicorn</a>

<a href="https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/gunicorn/">
    Deployando Django como WSGI
</a>


---

# Script de deployment

El script de deployment consiste en un conjunto de sentencias
que indican de una manera automatizada como:

1) Subir código

2) Aplicar las migraciones

2) Recolectar medios estáticos (en un lugar donde los "sirva" el webserver)

3) Instalar requerimientos del proyecto

4) Reinicar el servidor de aplicaciones

---

# Fabric

---

# pip install fabric

---

# fabfile.py

Fabric es un sistema de automatización de tareas en python de manera local y remota
(mediante SSH).

Un archivo fabfile básico consiste en:

    !python

    from fabric.api import env, local, run, task

    # Configurar la vairable env

    @task
    def listar_archivos():
        local('ls')

    @task
    def subir_archivos():
        put('ruta_local', 'ruta_remota')

Luego la ejecución es simple como

    !bash

    fab listar_archivos



---
# Como seguimos?

1) Cada alumno elige un subdomino de cursodedjango.com.ar o su propio domino (delegandolo
a 181.239.1.40). Ej: miprimeraapp.cursodedjango.com.ar


2) Cada alumno debe ejecutar enviar por correo su ~/.ssh/id-rsa.pub.
   Si no lo tiene, generarlo con ssh-keygen.

3) Una vez recibido el correo dirigido a
   <a href="mailto:capacitacion.dit+aprobacionweb@gmail.com">
       capacitacion.dit+aprobacionweb@gmail.com
   </a>
   con el id_rsa.pub y el subdominio/domino escojido,
   se otorga acceso a el usuario en el servidor donde
   su nombre de usuario será:
   primer letra del nombre continuado por el apellido.

   Ej: para juan perez, será jperez.

4) En respuesta al mail se ortorgará un puerto para el backend y se ayudará con un
   esqueleto de fabric y supervisor para controlar gunicorn.

5) Una vez que el sitio esté en línea, se da por aprobado el curso.