from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_type=models.CharField(max_length=50)

    def __str__(self):
        return self.category_type



class Story(models.Model):
    title=models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description=models.TextField(max_length=250)

    def __str__(self):
        return self.title



class StoryDetail(models.Model):
    content = models.TextField()
    story_id =  models.OneToOneField(Story, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content       


class Review(models.Model):
    content = models.TextField(max_length=250)
    story_id =  models.ForeignKey(Category, on_delete=models.CASCADE)
    user_review = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content       