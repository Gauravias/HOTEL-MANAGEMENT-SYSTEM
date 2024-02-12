from django.contrib import admin
from service.models import Service
class Gaurav(admin.ModelAdmin):
    list_display=('Service_icon','Service_title','Service_des')

admin.site.register(Service,Gaurav)    

# Register your models here.
