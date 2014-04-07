# Deployment

La puesta en produccion de un proyecto Django suele contar
de las siguientes estapas:

1) Escritura del script de deployment

2) Ejecución del script de deployment

---

# Estructura típica


<embed src="images/deployment_structure.svg" type="image/svg+xml" />

----


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
(mediante SSH). Cada tarea **es una función python**.

Las tareas deben ser funciones dentro de un archivo llamado fabfile.py:


Un archivo fabfile básico consiste en:

    !python
    from fabric.api import env, local, run, task
    # Configurar la vairable env

    @task
    def tarea_local():
        local('echo hola')

    @task
    def tarea_remota():
        run('echo hola')

Luego la ejecución es simple como

    !bash

    fab listar_archivos


---
# Deployando con fabric

Fabric tiene los siguientes comandos básicos:

**fabric.api.run('comando')** ejecuta en el servidor

**fabric.api.local('comando')** ejecuta en nuestra máquina

**fabric.api.put('fuente', 'destino')** ejecuta en nuestra máquina

**fabric.api.local('fuente', 'destino')** ejecuta en nuestra máquina


---
# Creando un fabfile

Para la comunicación remota es necesaria cierta configuración en la
variable **env**.

    !python
    from fabric.api import *

    env.user = 'gscalone'
    env.home = "/home/%s" % env.user
    env.project = 'myproject'
    env.project_dir = '/home/{user}/websites/{project}'.format(**env)
    env.venv_prefix = ('source /home/{user}/.virtualenvs/'
                      '{project}/bin/activate').format(**env)
    env.hosts = ['buscopartido.com.ar']
    env.use_ssh_config = True


---

    !python

    @task
    def instalar_proyecto():

        # run('mkdir -p ~/websites/{project}'.format(
        #     **env))
        local('pip freeze >requirements.txt')
        put('requirements.txt',
            '~/websites/{project}/requirements.txt'.format(
            **env))
        run('mkvirtualenv {project}'.format(
            **env))
        with cd(env.project_dir):
            with prefix(env.venv_prefix):
                run('pip install -r requirements.txt')

---

    !python
    @task
    def runserver(puerto=8888):
        with cd(env.project_dir):
            with prefix(env.venv_prefix):
                run('python manage.py runserver 0:{}'.format(puerto))

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