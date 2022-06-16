from django.shortcuts import render
from django.http import HttpResponse
from AppMTV.models import Familia
from django.template import loader

def familia(self):

    familiar1 = Familia(nombre= "Lucas", apellido= "Hartman", edad= 30, fecha_nacimiento= "1992-01-25")
    familiar2 = Familia(nombre= "Julian", apellido= "Hartman", edad= 25, fecha_nacimiento= "1997-06-15")
    familiar3 = Familia(nombre= "Pedro", apellido= "Hartman", edad= 10, fecha_nacimiento= "2012-08-13")

    familiar1.save()
    familiar2.save()
    familiar3.save()



    diccionario = {
    'nombre1':familiar1.nombre, 'apellido1':familiar1.apellido, 'edad1':familiar1.edad, 'fecha_de_nacimiento1':familiar1.fecha_nacimiento, 
    'nombre2':familiar2.nombre, 'apellido2':familiar1.apellido, 'edad2':familiar1.edad, 'fecha_de_nacimiento2':familiar1.fecha_nacimiento,
    'nombre3':familiar1.nombre, 'apellido3':familiar1.apellido, 'edad3':familiar1.edad, 'fecha_de_nacimiento3':familiar1.fecha_nacimiento
    }

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)


    return HttpResponse(documento)
