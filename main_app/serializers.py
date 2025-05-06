from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework import serializers
from .models import Story, Category, Review , Like , Author

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
    user_review = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'story_id', 'user_review', 'content']
        read_only_fields = ['user_review']




class StorySerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Story
        fields = '__all__'

    def update(self, instance, validated_data):
        request = self.context.get('request')
        if request and request.user:
            validated_data['author'] = request.user
        return super().update(instance, validated_data)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        return super().create(validated_data)
    


class CategorySerializer(serializers.ModelSerializer):
    story = StorySerializer (read_only = True)

    class Meta:
        model = Category
        fields = '__all__'



class LikeSerializer(serializers.ModelSerializer):
    story_liked = StorySerializer(read_only=True)
    author_liked = UserSerializer(read_only=True)
    user_fav  = UserSerializer(read_only=True)


    class Meta:
        model = Like
        fields = '__all__'



class AuthorSerializer(serializers.ModelSerializer):
    story_posted = StorySerializer(read_only=True)
    author_name = UserSerializer(read_only=True)
    likes  = LikeSerializer(read_only=True)

    
    class Meta:
        model = Author
        fields = '__all__'