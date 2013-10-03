.. Introducción a Desarrollo de Aplicaciones Web documentation master file, created by
   sphinx-quickstart on Thu Oct  3 11:32:19 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introducción a Desarrollo de Aplicaciones Web
=============================================


.. figure:: /_static/img/bg1.jpg
    :class: fill


..

    .. authors:: Defossé Nahuel, van Haaster Diego Marcos

    Contenidos:

    .. toctree::
       :maxdepth: 2




Conceptos básicos de aplicaciones Web
=====================================


Una aplicacción web consiste en un servidor y un cliente que hablan en un protocolo
llamado HTTP.

Cuando un navegador accede a ``google.com``, le dice algo como:


Diálogo cliente a servidor
==========================

.. code-block:: bash

    GET / HTTP/1.1
    Host: www.google.com.ar
    Connection: keep-alive
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    User-Agent: Mozilla/5.0 (X11; Linux x86_64)
    Accept-Encoding: gzip,deflate,sdch
    Accept-Language: es-419,es;q=0.8,en;q=0.6


Respuesta servidor a cliente
----------------------------

.. code-block:: bash

    source