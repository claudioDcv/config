from django import forms
from .models import Plant, Control, PlantType, Group

class PlantForm(forms.ModelForm):

    code = forms.CharField(label='Código', max_length=100)
    birthdate = forms.DateField(
        label='Fecha de nacimiento',
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'autocomplete': 'off',
            'class': 'form-control datepicker datepicker-input',
        })
    )
    death_date = forms.DateField(
        label='Fecha de muerte',
        required=False,
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'autocomplete': 'off',
            'class': 'form-control datepicker datepicker-input-nullable',
        })
    )

    def __init__(self, *args, **kwargs):
        super(PlantForm, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs = { 'class': 'form-control' }
        # self.fields['group'].widget.attrs = { 'class': 'form-control' }
        # self.fields['group'].queryset = Group.objects.none()

    class Meta:
        model = Plant
        exclude = ('owner', 'group', 'slug', 'plant_type', 'is_deleted')


class ControlForm(forms.ModelForm):

    capture_date = forms.DateTimeField(
        label='* Fecha y hora de control',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
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
        label='* Temperatura en C°',
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control temperature-color',
            'placeholder': 'Ingrese Temperatura en Celcius',
        })
    )
    humidity = forms.DecimalField(
        label='* Humedad %',
        max_digits=5, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control humidity-color',
            'placeholder': 'Ingrese Humedad en porcentaje',
        })
    )
    height = forms.DecimalField(
        label='* Altura Cm (123cm)',
        max_digits=7, decimal_places=2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control height-color',
            'placeholder': 'Ingrese Altura (centimetros)',
        })
    )
    weight = forms.DecimalField(
        label='* Peso KG (Ej: 12.244kg)',
        max_digits=5, decimal_places=3,
        widget=forms.NumberInput(attrs={
            'class': 'form-control weight-color',
            'placeholder': 'Ingrese Peso (KG)',
        })
    )

    class Meta:
        model = Control
        exclude = ('plant', 'is_deleted', 'solutions')
    
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ControlForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        # self.fields.keyOrder = ['capture_date', 'temperature', 'humidity', 'weight', 'description']

        self.fields['description'].required = False


class GroupForm(forms.ModelForm):

    label = forms.CharField(
        label='Nombre',
        max_length=100,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nombre de su grupo',
        })
    )

    class Meta:
        model = Group
        exclude = ('owner', 'is_deleted')