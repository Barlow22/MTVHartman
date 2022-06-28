from django import forms

class Clientes_form(forms.Form):
    
    nombre_fantasia = forms.CharField(max_length=40)
    razon_social = forms.CharField(max_length=40)
    cuit = forms.IntegerField()
    calle = forms.CharField(max_length=40)
    altura = forms.IntegerField()
    fecha_alta = forms.DateField()

class Proveedores_form(forms.Form):
    
    nombre_fantasia = forms.CharField(max_length=40)
    razon_social = forms.CharField(max_length=40)
    cuit = forms.IntegerField()
    calle = forms.CharField(max_length=40)
    altura = forms.IntegerField()
    fecha_alta = forms.DateField()


class Articulos_form(forms.Form):

    codigo = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    precio = forms.IntegerField()
    stock = forms.IntegerField()


class Pagos_form(forms.Form):

    monto = forms.IntegerField()
    forma_pago = forms.CharField(max_length=40)
    fecha_pago = forms.DateField()