from django import forms
from gestorDeuda.models import Deudas, DetallesDeuda
from django.core import validators

class Deuda(forms.Form):

    nombre = forms.CharField(validators=[validators.MinLengthValidator(3),validators.MaxLengthValidator(20)])
    deudaTotal=forms.IntegerField()
    descripcion=forms.CharField()

    nombre.widget.attrs['class'] = 'form-control'
    deudaTotal.widget.attrs['class'] = 'form-control'


class Deuda(forms.ModelForm):

    nombre = forms.CharField(validators=[validators.MinLengthValidator(3),validators.MaxLengthValidator(20)])
    deudaTotal=forms.IntegerField()

    
    nombre.widget.attrs['class'] = 'form-control'
    deudaTotal.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Deudas
        fields = '__all__'
        widgets = {'usuario': forms.HiddenInput()} 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].required = False

class DetalleDeuda(forms.Form):

    cantidadCuota = forms.IntegerField()
    descripcion=forms.CharField()

    cantidadCuota.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    
class DetalleDeuda(forms.ModelForm):

    cantidadCuota = forms.IntegerField()
    descripcion=forms.CharField()

    cantidadCuota.widget.attrs['class'] = 'form-control'
    descripcion.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = DetallesDeuda
        fields = '__all__'
        widgets = {
            'deuda': forms.HiddenInput(),
            'valorMensual': forms.HiddenInput(),
            'calculoValor': forms.HiddenInput(),
            'finalizada': forms.HiddenInput()
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deuda'].required = False
        self.fields['valorMensual'].required = False
        self.fields['calculoValor'].required = False
        self.fields['finalizada'].required = False