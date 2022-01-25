from csv import list_dialects
from django.contrib import admin
from .models import Owner,PropertyUsage,OwnershipStatus,SingleProperty
# Register your models here.



class SinglePropertyAdmin(admin.ModelAdmin):
    list_display=("name","location","owner","propertyStatus","image")


class OwnerAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname",)

admin.site.register(Owner,OwnerAdmin),
admin.site.register(PropertyUsage),
admin.site.register(OwnershipStatus),
admin.site.register(SingleProperty,SinglePropertyAdmin),