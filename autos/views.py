# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Q

from autos.models import *
from autos.forms import *

import datetime

def start(request):
    now = datetime.datetime.now()
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        search = True
        amanufacts = AManufact.objects.filter(name__icontains=q)
        amodels = AModel.objects.filter(Q(name__icontains = q) | Q(amanufact__in = amanufacts))
        aitems = AItem.objects.filter(amodel__in = amodels)
    else:
        q=""
        search = False
        aitems = AItem.objects.all()
    return render_to_response('start.html', {'username' : request.user.username, 'current_date': now,'text_enabled': search, 'request' : q, 'aitems': aitems})

from django.http import HttpResponseRedirect
from django.contrib import auth

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect("/")
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/")

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/")

def prototype(request):
    return render_to_response('prototype.js')

def feed_models(request, make_id): 
    make = AManufact.objects.get(id = make_id) 
    models = AModel.objects.filter(amanufact = make) 
    return render_to_response('feeds/models.txt', {'models':models})

def item_add_form(request):
    if request.method == 'POST':
        form = AItemForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            amodel = AModel.objects.get(id = cd['amodel']) 
            try:
                AItem.objects.create(
                    amodel = amodel, 
                    color = cd['color'], 
                    hp = cd['hp'], 
                    mfdate = cd['mfdate'])
                return render_to_response('success.html')
            except:
                return render_to_response('fail.html')
        return render_to_response('aitem_form.html', {'form': form, 'amanufact1' : AManufact.objects.all()})
    else:
        form = AItemForm()
    return render_to_response('aitem_form.html', {'form':form, 'amanufact1':AManufact.objects.all(), 'action':'add'})

def item_edit_form(request):
    if request.method == 'POST':
        form = AItemForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            aitem = AItem.objects.get(id = cd['aid'])
            aitem.amodel = AModel.objects.get(id = cd['amodel']) 
            aitem.color = cd['color']
            aitem.hp = cd['hp']
            aitem.mfdate = cd['mfdate']
            try:
                aitem.save()
                return render_to_response('success.html')
            except:
                return render_to_response('fail.html')
        return render_to_response('aitem_form.html', {'form': form, 'amanufact1' : AManufact.objects.all()})
    else:
        aid = 0
        if 'item_id' in request.GET and request.GET['item_id']:
            try:
                aid = int(request.GET['item_id'])
            except:
                return HttpResponseRedirect("/")
        else: 
            return HttpResponseRedirect("/")
        aitem = AItem.objects.get(id=aid)
        amodel = aitem.amodel
        amanufact = amodel.amanufact
        form = AItemForm(initial={'aid':aid, 'amanufact':amanufact, 'amodel':amodel, 'color':aitem.color, 'hp':aitem.hp, 'mfdate':aitem.mfdate})
    return render_to_response('aitem_form.html', {'form':form, 'amanufact1':AManufact.objects.all(), 'amanufact2':amanufact, 'amodel1':amodel, 'action':'edit'})

def delete_item(request):
    if 'item_id' in request.GET and request.GET['item_id']:
        item_id = request.GET['item_id']
        item = AItem.objects.filter(id = item_id)[0]
        try:
            item.delete()
            return render_to_response('success.html')
        except:
            pass
    return render_to_response('fail.html')
        

def preview(request, itm, selected):
    try:
        item_id = int(itm)
        selected = int(selected)
    except ValueError:
        return HttpResponseRedirect("/")
    item = AItem.objects.get(id = item_id)
    imglist = APreview.objects.filter(aitem = item)
    if imglist.count() > 0:
        for iimg in imglist:
            iimg.create_thumb()
        viewimg=imglist[selected].img
        no_items = False
        return render_to_response('preview.html', {'no_items': False, 'itm_id' : item_id, 'viewimg' : viewimg,'imglist' : imglist})
    return render_to_response('preview.html', {'no_items': True})

