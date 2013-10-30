# Modelos

.fx: title

---

# Modelos

.fx: smallbullet

Los modelos encapsulan la información referente al dominio de la aplicación web.
Compuestos por campos generalmente cada modelo mapea a una única tabla de la base de datos.

* Cada modelo es una clase en Python que hereda de django.db.models.Model.

* Cada atributo del modelo se corresponde con una columna en la base de datos.

* Con esto Django genera automáticamente una API de acceso a datos.

## Bases de datos

Django tiene 4 **backends** oficiales MySQL, SQLite, Postgres y Oracle.

Existen otros backends creados por la comunidad para Firebird, ODBC, SQL Server y bases
de datos no relacionales.

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

# Modelos - Ejemplo


    !python

    class Persona(models.Model):
        nombre = models.CharField(max_length=50)


    class Mascota(models.Model):
        # Constantes
        MACHO, HEMBRA = 'm', 'h'
        SEXO_CHOICES = (
            (MACHO, 'Macho'), (HEMBRA, 'Hembra')
        )
        duenio = models.ForeignKey(Persona, null=True, blank=True)
        raza = models.ForeignKey('Especie') # Relación hacia adelante
        sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    class Especie(models.Model):
        nombre = models.CharField(max_length=50)
        domesticable = models.BooleanField(default=True)

    class Raza(models.Model):
        nombre = models.CharField(max_length=50)
        especie = models.ForeignKey(Especie)

---

# Ejemplos - Contiunación

## Validación

    !bash
    python manage.py validate

    0 errors found

## Creación de tablas

    !bash
    python manage.py syncdb

    Creating table common_persona
    Creating table common_mascota
    Creating table common_especie
    Creating table common_raza


---

# Equivalencia en SQL

<center>
    <img src="images/sql.gif" style="padding: 20%;">
</center>

---

# Equivalencia SQL


    !sql
    BEGIN;
    CREATE TABLE "common_persona" (
        "id" integer NOT NULL PRIMARY KEY,
        "nombre" varchar(50) NOT NULL
    );
    CREATE TABLE "common_mascota" (
        "id" integer NOT NULL PRIMARY KEY,
        "duenio_id" integer REFERENCES "common_persona" ("id"),
        "raza_id" integer NOT NULL,
        "sexo" varchar(1) NOT NULL
    );
    CREATE TABLE "common_especie" (
        "id" integer NOT NULL PRIMARY KEY,
        "nombre" varchar(50) NOT NULL,
        "domesticable" bool NOT NULL
    );
    CREATE TABLE "common_raza" (
        "id" integer NOT NULL PRIMARY KEY,
        "nombre" varchar(50) NOT NULL
    );
    COMMIT;

Y esto sin contar los índices!

---

# Modelos - Uso

Los modelos herdean el comportamiento de *models.Model*, métodos como **save** y
**delete** ya están disponibles para ser utilizados.

    !python

    from miapp.models import Persona

    p = Persona(nombre='Dundee')
    p.save()

    p.id
    # -> 1

    p.save()
    p.id
    # -> 1

    q = Persona()
    q.nombre = 'Anonio'
    # -> None
    q.save()

    q.nombre = 'Antonieta'
    q.save()
    q.delete()

---

# Otras opciones para los modelos

1. Al ser clases los modelos pueden tener métodos que efectuen alguna acción en función
   de los datos que contengan, por ejemplo, la representación como cadena:


        !python

        class Persona(models.Model):
            nombre = models.CharField(max_length=50)
            def __unicode__(self):
                return "Soy %s" % self.nombre

2. <a href="https://docs.djangoproject.com/en/1.5/ref/models/options/">
    Metainformación</a>
    Permite agregar información como el nombre de la tabla en la base de datos,
    una etiqueta de texto, orden por defecto, restricciones de unicidad, etc.

        !python

        class Registro(models.Model):
            fecha = models.DateField()
            class Meta:
                verbose_name = "Registro de actividad"
                verbose_name_plural = "Registros de actividad"
                ordering = '-fecha'

---

# Managers

Django provee una propiedad en todos los modelos que
nos permite hacer SELECT, INSERT, UPDATE y DELETE muy facilmente.

    !python

    Persona.objects.create(nombre='Jose')

    Persona.objects.filter(nombre__istartswith='jos')

    mascotas = Mascota.objects.exclude(sexo=Mascota.MACHO)

    mascotas.filter(raza=Raza).delete()

---

# Managers (cont)

<img src="images/perezoso.jpg">

## Evaluación perezoa

Los managers devuelven objetos del tipo QuerySet con el SQL
calculado pero no evaluado (no se ejecutó sobre la base),
cuando se recorre por primera vez, se ejecuta la consulta.

