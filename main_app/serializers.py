from django.contrib.auth.models import User
from rest_framework import serializers


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


# class CatSerializer(serializers.ModelSerializer):
#     photo = PhotoSerializer(read_only=True)
#     toys = ToySerializer(many=True, read_only=True)
#     user = serializers.PrimaryKeyRelatedField(read_only=True)

#     class Meta:
#         model = Cat
#         fields = '__all__'