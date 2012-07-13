# -*- coding: utf-8 -*-
from django import forms
from autos.models import *

class DynamicChoiceField(forms.ChoiceField): 
    def clean(self, value): 
        return value

class AItemForm(forms.Form):
    aid = forms.IntegerField(widget=forms.HiddenInput(), initial=-1)
    amanufact = forms.ModelChoiceField(queryset=AManufact.objects.all(), label='Производитель')
    #amanufact = forms.ChoiceField(label='Производитель')
    amodel = DynamicChoiceField(label='Модель')
    color = forms.CharField(label='Цвет')
    hp = forms.IntegerField(label='Мощность')
    mfdate = forms.DateField(label='Дата выпуска')

