from django.contrib import admin
from .models import Waterorder

class WaterorderAdmin(admin.ModelAdmin):
    list_display = ('grower','cfs','hours')

admin.site.register(Waterorder, WaterorderAdmin)
