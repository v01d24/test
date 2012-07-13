#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Truck(models.Model):
    capacity = models.IntegerField(verbose_name='Грузоподъёмность')
    horsepower = models.IntegerField(verbose_name='Сила')

    def __unicode__(self):
        return "[%d kg, %d hp]" % (self.capacity, self.horsepower) 

class Car(models.Model):
    body_type = models.CharField(max_length=128, verbose_name='Тип кузова')
    speed = models.IntegerField(verbose_name='Скорость')
    doors = models.IntegerField(verbose_name='Количество дверей')

    def __unicode__(self):
        return "[%s, %d doors, %d km/h]" % (self.body_type, self.doors, self.speed) 

class Item(models.Model):
    modelname = models.CharField(max_length=128, verbose_name='Модель')
    item_type = models.ForeignKey(ContentType, blank=True, null=True, verbose_name="Type")
    item_id = models.PositiveIntegerField(blank=True, null=True, editable=True, verbose_name=u"Link")
    item = generic.GenericForeignKey('item_type', 'item_id')

    def __unicode__(self):
        model = self.item
        return "%s %s %s" % (self. item_type, self.modelname, model)       
