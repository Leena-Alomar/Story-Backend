from django.contrib import admin
from .models import Category,Story,StoryDetail,Review


# Register your models here.
admin.site.register(Category)
admin.site.register(Story)
admin.site.register(StoryDetail)
admin.site.register(Review)