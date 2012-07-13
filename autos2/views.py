# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from autos2.models import *
from autos2.forms import *

def catalog(request):
    return render_to_response('catalog.html', {'items':Item.objects.all()})

def catalog_add(request):
    if request.method == 'POST':
        if 'type' in request.POST and request.POST['type']:
            id_type = int(request.POST['type'])
        else: 
            return HttpResponseRedirect('/catalog2/') 
        if (id_type == 0):
            form = CarForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                car = Car()
                car.body_type=cd['body_type']
                car.speed=cd['speed']
                car.doors=cd['doors']
                car.save()
                item = Item(item = car, modelname = cd['modelname'])
                item.save()
        else:
            form = TruckForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                truck = Truck()
                truck.capacity=cd['capacity']
                truck.horsepower=cd['horsepower']
                truck.save()
                item = Item(item = truck, modelname = cd['modelname'])
                item.save()
        return HttpResponseRedirect('/catalog2/')
    else:
        form = UniversalForm()
    return render_to_response('catalog_edit.html', {'form': form})

def catalog_edit(request, item_id):
    if request.method == 'POST':
        if 'type' in request.POST and request.POST['type']:
            id_type = int(request.POST['type'])
        else: 
            return HttpResponseRedirect('/catalog2/') 
        if (id_type == 0):
            form = CarForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                item = Item.objects.get(id = cd['item_id'])
                if item.item_type == ContentType.objects.get_for_model(Car):
                    car = item.item
                else:
                    item.item.delete()
                    car = Car()
                car.body_type=cd['body_type']
                car.speed=cd['speed']
                car.doors=cd['doors']
                car.save()
                item.item = car
                item.modelname = cd['modelname']
                item.save()
        else:
            form = TruckForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                item = Item.objects.get(id = cd['item_id'])
                if item.item_type == ContentType.objects.get_for_model(Truck):
                    truck = item.item
                else:
                    item.item.delete()
                    truck = Truck()
                truck.capacity=cd['capacity']
                truck.horsepower=cd['horsepower']
                truck.save()
                item.item = truck
                item.modelname = cd['modelname']
                item.save()

        return HttpResponseRedirect('/catalog2/')
    else:
        item = Item.objects.get(id = item_id)
        model = item.item
        selected = 0
        if item.item_type == ContentType.objects.get_for_model(Car):
            form = UniversalForm(initial={'item_id':item.id, 'id_type':0, 'modelname':item.modelname, 'body_type':model.body_type, 'speed':model.speed, 'doors':model.doors})
        else:
            selected = 1
            form = UniversalForm(initial={'item_id':item.id, 'id_type':1, 'modelname':item.modelname, 'capacity':model.capacity, 'horsepower':model.horsepower})
    return render_to_response('catalog_edit.html', {'form': form, 'selected':selected})

def catalog_delete(request, item_id):
    item = Item.objects.get(id = item_id)
    item.item.delete()
    item.delete()
    return HttpResponseRedirect('/catalog2/')
