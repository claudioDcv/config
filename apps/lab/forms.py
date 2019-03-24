from django import forms
from .models import ElementSolution, Solution

class SolutionForm(forms.ModelForm):

    description = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese Descripción',
        })
    )

    class Meta:
        model = ElementSolution
        exclude = ('owner',)


class ElementSolutionForm(forms.ModelForm):

    class Meta:
        model = ElementSolution
        exclude = ('owner',)