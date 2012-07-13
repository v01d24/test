#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class AManufact(models.Model):
    name = models.CharField(max_length=128, verbose_name='Производитель')

    def __unicode__(self):
        return self.name

class AModel(models.Model):
    name = models.CharField(max_length=128, verbose_name='Модель')
    amanufact = models.ForeignKey(AManufact, verbose_name='Производитель')
    smfdate = models.DateField(verbose_name='Начало выпуска модели')
    stillmf = models.BooleanField(verbose_name='Выпускается в настоящее время')

    def __unicode__(self):
        return "%s %s" % (self.amanufact.name, self.name) 

class AItem(models.Model):
    amodel = models.ForeignKey(AModel, verbose_name='Модель')
    color = models.CharField(max_length=20, verbose_name='Цвет')
    hp = models.IntegerField(verbose_name='Мощность')
    mfdate = models.DateField(verbose_name='Дата выпуска')

    def __unicode__(self):
        return "%s %s (%d)" % (self.amodel.amanufact.name, self.amodel.name, self.mfdate.year) 

import os
import PIL
from PIL import Image
from cStringIO import StringIO

class APreview(models.Model):
    aitem = models.ForeignKey(AItem, verbose_name='Экземпляр')
    img = models.ImageField(upload_to = 'images/')
    thumb = models.ImageField(upload_to='thumbs/', blank=True, null=True)
    def save(self):
    #Размер миниатюры 
        THUMBNAIL_SIZE = (100, 100)
    #Далее, открытие файла с изображением, для последующей работы с ним 
        image = PIL.Image.open(self.img)
    #Если не RGB то сделать RGB 
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
    #Непосредственно, само создание миниатюры 
        image.thumbnail(THUMBNAIL_SIZE, PIL.Image.ANTIALIAS)
    #Создание временного файла, куда помещается созданная миниатюра
        temp_handle = StringIO()
    #Сохранение во временном файле (интересно звучит) 
        image.save(temp_handle, 'png')
        temp_handle.seek(0)
    #Сохранение в так называемом "Simple-файле", для передачи его в upload
        from django.core.files.uploadedfile import SimpleUploadedFile
        suf = SimpleUploadedFile(os.path.split(self.img.name)[-1],
        temp_handle.read(), content_type='image/png')
        self.thumb.save(suf.name+'.png', suf, save=False)
 
    #Сохранение в модели "simple-файла"
        super(APreview, self).save()

    def create_thumb(self):  
        if not self.thumb:  
            image = PIL.Image.open(self.img) 
            # Create the thumbnail of dimension size  
            THUMBNAIL_SIZE = (100, 100)
            image.thumbnail(THUMBNAIL_SIZE, PIL.Image.ANTIALIAS) 
            # Get the directory name where the temp image was stored  
            # by urlretrieve  
            dir_name = os.path.dirname(image[0])  
            # Get the image name from the url  
            img_name = os.path.basename(self.image.url)  
            # Save the thumbnail in the same temp directory   
            # where urlretrieve got the full-sized image,   
            # using the same file extention in os.path.basename()  
            t_img.save(os.path.join(dir_name, "thumb" + img_name))  
            # Save the thumbnail in the media directory, prepend thumb    
            self.mini_img.save(os.path.basename("thumb" + self.image.url),File(open(os.path.join(dir_name, "thumb" + img_name))))

