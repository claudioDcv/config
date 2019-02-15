from django import forms
from .models import Plant, Control

class PlantForm(forms.ModelForm):

    code = forms.CharField(label='Código', max_length=100)
    birthdate = forms.DateField(label='Fecha de nacimiento', required=False)
    death_date = forms.DateField(label='Fecha de muerte', required=False)

    def __init__(self, *args, **kwargs):
        super(PlantForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs = { 'class': 'form-control' }
        self.fields['birthdate'].widget.attrs = { 'class': 'form-control' }
        self.fields['death_date'].widget.attrs = { 'class': 'form-control' }

    class Meta:
        model = Plant
        exclude = ('owner', 'slug' )


class ControlForm(forms.ModelForm):

    capture_date = forms.DateTimeField(
        label='Fecha y hora de control',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

    description = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Descripción',
        })
    )

    temperature = forms.DecimalField(
        label='Temperatura',
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control temperature-color',
            'placeholder': 'Ingrese Temperatura',
        })
    )
    humidity = forms.DecimalField(
        label='Humedad',
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control humidity-color',
            'placeholder': 'Ingrese Humedad',
        })
    )
    height = forms.DecimalField(
        label='Altura',
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control height-color',
            'placeholder': 'Ingrese Altura (centimetros)',
        })
    )
    weight = forms.DecimalField(
        label='Peso',
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control weight-color',
            'placeholder': 'Ingrese Peso (gramos)',
        })
    )

    class Meta:
        model = Control
        exclude = ('plant', )