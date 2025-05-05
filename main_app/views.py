from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer,StorySerializer,CategorySerializer,ReviewSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from .models import Story, Category, Review
from django.shortcuts import get_object_or_404

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the cat-collector api home route!'}
    return Response(content)
    
# User Registration
class CreateUserView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def create(self, request, *args, **kwargs):
    try:
      response = super().create(request, *args, **kwargs)
      user = User.objects.get(username=response.data['username'])
      refresh = RefreshToken.for_user(user)
      content = {'refresh': str(refresh), 'access': str(refresh.access_token), 'user': response.data }
      return Response(content, status=status.HTTP_201_CREATED)
    except Exception as err:
      return Response({ 'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(APIView):

  def post(self, request):
    try:
      username = request.data.get('username')
      password = request.data.get('password')
      user = authenticate(username=username, password=password)
      if user:
        refresh = RefreshToken.for_user(user)
        content = {'refresh': str(refresh), 'access': str(refresh.access_token),'user': UserSerializer(user).data}
        return Response(content, status=status.HTTP_200_OK)
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# User Verification
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    try:
      user = User.objects.get(username=request.user.username)
      try:
        refresh = RefreshToken.for_user(user)
        return Response({'refresh': str(refresh),'access': str(refresh.access_token),'user': UserSerializer(user).data}, status=status.HTTP_200_OK)
      except Exception as token_error:
        return Response({"detail": "Failed to generate token.", "error": str(token_error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as err:
      return Response({"detail": "Unexpected error occurred.", "error": str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#Category Views
class CategoryIndexView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer

    def get(self, request):
      try:
        queryset = Category.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
      except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    lookup_field = 'id'

def get(self, request,category_id):
  try:
    category = get_object_or_404(Category, id=category_id)
    Stories = Story.objects.filter(category=category_id)
    return Response(serializer.data, status=status.HTTP_200_OK)
  except Exception as err:
    return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


  def delete(self, request, category_id):
    try:
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CategoryAddStoryDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StorySerializer


    def post(self, request, category_id):
        try:
            category = get_object_or_404(Category, id=category_id)
            serializer = self.serializer_class(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(category=category, author=request.user)
                queryset = Story.objects.filter(category=category_id)
                stories = StorySerializer(queryset, many=True)
                return Response(stories.data, status=status.HTTP_201_CREATED)
            else:
                print("Validation errors:", serializer.errors) 
                print(request.author)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class StoryView(APIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = StorySerializer

  def get(self, request):
    try:
      queryset = Story.objects.all()
      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class StoryDetail(APIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = StorySerializer
  lookup_field = 'id'
  
  def get(self, request, story_id):
    try:
      story = get_object_or_404(Story, id=story_id)
      return Response(self.serializer_class(toy).data, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    
  def put(self, request, story_id):
    try:
        story = get_object_or_404(Story, id=story_id)
        serializer = self.serializer_class(story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


  def delete(self, request, story_id):
    try:
        story = get_object_or_404(Story, id=story_id)
        story.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)