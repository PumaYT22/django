from django.contrib import admin
from .models import Books,PublishingHouse,Category
# Register your models here.

admin.site.register(Books)
admin.site.register(PublishingHouse)
admin.site.register(Category)
