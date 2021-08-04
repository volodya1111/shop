from django.contrib import admin
from.models import Phone, Laptop, Watch
from.models import Category

admin.site.register(Phone)
admin.site.register(Laptop)
admin.site.register(Watch)
admin.site.register(Category)
