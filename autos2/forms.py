# -*- coding: utf-8 -*-
from django import forms
from autos2.models import *

class TruckForm(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput(), initial=-1)
    #id_type = forms.ChoiceField(widget=forms.HiddenInput(), initial=0)
    modelname = forms.CharField(label='Производитель')
    capacity = forms.IntegerField(label='Грузоподъёмность')
    horsepower = forms.IntegerField(label='Сила')

class CarForm(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput(), initial=-1)
    #id_type = forms.ChoiceField(widget=forms.HiddenInput(), initial=0)
    modelname = forms.CharField(label='Производитель')
    body_type = forms.CharField(label='Тип кузова')
    speed = forms.IntegerField(label='Скорость')
    doors = forms.IntegerField(label='Количество дверей')

class UniversalForm(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput(), initial=-1)
    id_type = forms.ChoiceField(widget=forms.HiddenInput(), initial=0)
    modelname = forms.CharField(label='Производитель')
    capacity = forms.IntegerField(label='Грузоподъёмность')
    horsepower = forms.IntegerField(label='Сила')
    body_type = forms.CharField(label='Тип кузова')
    speed = forms.IntegerField(label='Скорость')
    doors = forms.IntegerField(label='Количество дверей')
