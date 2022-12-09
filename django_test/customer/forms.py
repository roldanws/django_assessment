from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['name', 'paternal_surname', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'paternal_surname': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido Paterno'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo  '}),
        }
        labels = {
            'name':'', 'email':'', 'paternal_surname': ''
        }