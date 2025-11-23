from django.contrib import admin
from .models import useddata
@admin.register(useddata)
class useddataAdmin(admin.ModelAdmin):
    list_display=['id','username','Email','password','ConfirmPassword']

# Register your models here.
