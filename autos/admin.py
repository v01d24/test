from django.contrib import admin
from pr1.autos.models import AManufact, AModel, AItem, APreview

class ItemOptions(admin.ModelAdmin):
    #list_display = ('name', 'year', 'hp')
	date_hierarchy = 'mfdate'

admin.site.register(AManufact)
admin.site.register(AModel)
admin.site.register(AItem, ItemOptions)
admin.site.register(APreview)
