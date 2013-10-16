# encoding: utf-8

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return "Soy %s %s" % (self.nombre,
                              self.apellido)

n = Persona("Nahuel", "Defossé")
d = Persona("Diego", "van Haaster")

for persona in [n, d]:
    print "%s es una persona" % persona