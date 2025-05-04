from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework import serializers
from .models import Story, Category, Review

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


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        
class StorySerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)  # <- ✅ THIS IS CRUCIAL

    class Meta:
        model = Story
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)



class CategorySerializer(serializers.ModelSerializer):
    story = StorySerializer (read_only = True)

    class Meta:
        model = Category
        fields = '__all__'

