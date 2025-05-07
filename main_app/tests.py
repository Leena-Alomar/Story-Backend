from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Category, Story, Review, Like, Author

class ViewsTest(TestCase):
    def setUp(self):
    
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.other_user = User.objects.create_user(username='otheruser', password='abc123')
        self.category = Category.objects.create(category_type='Science Fiction')
        
    
        self.story = Story.objects.create(
            title="Mars Adventure",
            category=self.category,
            author=self.user,
            description="An adventure story on Mars",
            content="Once upon a time...",
            photo_url="http://example.com/mars.jpg"
        )
        

        self.review = Review.objects.create(
            content="Great story!",
            story_id=self.story,
            user_review=self.user
        )
        

        self.like = Like.objects.create(
            story_liked=self.story,
            user_fav=self.user,
            author_liked=self.user
        )

 
        self.author = Author.objects.create(
            author_name=self.user,
            story_posted=self.story,
            likes=self.like,
            profile_pic="http://example.com/profile.jpg"
        )

        self.client.login(username='testuser', password='12345')  



    def test_category_list_view(self):
        url = reverse('category-index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('category_type', str(response.content))

    def test_category_detail_view(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.category.category_type, str(response.content))

    def test_story_detail_view(self):
        url = reverse('story-detail', args=[self.story.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.story.title, str(response.content))

    def test_create_story_view(self):
        url = reverse('story-detail', args=[self.category.id])  # URL for creating a new story
        data = {
            'title': 'New Story',
            'category': self.category.id,
            'author': self.user.id,
            'description': 'A brand new story',
            'content': 'This is the content of the new story.',
            'photo_url': 'http://example.com/new_story.jpg'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('title', response.data)

    def test_create_review_view(self):
        url = reverse('review-detail', args=[self.story.id]) 
        data = {'content': 'Amazing!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('content', response.data)

    def test_like_story_view(self):
        url = reverse('like-detail', args=[self.story.id])  
        data = {'user_fav': self.user.id, 'author_liked': self.user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('user_fav', response.data)

    def test_author_view(self):
        url = reverse('author-index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.user.username, str(response.content))

    def test_delete_story(self):
        url = reverse('story-detail', args=[self.story.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': True})

    def test_user_registration(self):
        url = reverse('signup')
        data = {'username': 'newuser', 'password': 'newpassword123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_user_login(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        url = reverse('token_refresh')
        data = {'refresh': 'your_refresh_token_here'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_delete_category(self):
        url = reverse('category-detail', args=[self.category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'success': True})
