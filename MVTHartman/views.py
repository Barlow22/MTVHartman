from django.http import HttpResponse
from datetime import datetime
from django.template import Template, context
from django.template import loader

def template1(self):
    nom = 'Lucas'
    ap = 'Hartman'
    diccionario = {'nombre':nom, 'apellido':ap}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

