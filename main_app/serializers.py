from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Story, Category, Review, StoryDetail 

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']  
        )
      
        return user


class StorySerializer(serializers.ModelSerializer):
    review = PhotoSerializer(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Story
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    story = StorySerializer (read_only = True)

    class Meta:
        model = Category
        fields = '__all__'

class StoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoryDetail
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
