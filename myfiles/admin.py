from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminSub(admin.ModelAdmin):
    list_display = ['id','ism','username','familya','tg_id']

admin.site.register(Subscribe,AdminSub)
