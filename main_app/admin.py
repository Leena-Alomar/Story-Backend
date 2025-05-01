from django.contrib import admin
from .models import Category,Story,Review


# Register your models here.
admin.site.register(Category)
admin.site.register(Story)
admin.site.register(Review)