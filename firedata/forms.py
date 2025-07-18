# forms.py
from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(widget=forms.PasswordInput, label='password')

class BurningEventForm(forms.ModelForm):
    # Campos auxiliares, NÃO pertencem ao modelo BurningEvent
    conservation_unit_name = forms.CharField(label="Conservation Unit Name", max_length=200)
    management_unit = forms.ModelChoiceField(queryset=ManagementUnit.objects.all(), label="Management Unit")
    regional_group = forms.ModelChoiceField(queryset=RegionalGroup.objects.all(), label="Regional Group")

    class Meta:
        model = BurningEvent
        # Apenas campos que existem no modelo BurningEvent
        fields = [
            'wildfire_area',
            'prescribed_burn_area',
            'controlled_burn_area',
            'firebreak_area',
            'natural_fire_area',
            'isolated_indigenous_area',
            'area_total',
            'total_prevention_area',
            'total_firefighting_area',
        ]

class ConservationUnitForm(forms.ModelForm):
    class Meta:
        model = ConservationUnit
        fields = [
            'name',
            'management_unit',
            'regional_group',
            'area_in_uc',
            'percent_fire_affected_in_uc',
        ]

class ManagementUnitForm(forms.ModelForm):
    class Meta:
        model = ManagementUnit
        fields = [
            'name',
            'regional_group'
        ]
