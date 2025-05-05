from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('categories/', views.CategoryIndexView.as_view(), name='category-index'),
    path('users/signup/', views.CreateUserView.as_view(), name='signup'),
    path('users/login/', views.LoginView.as_view(), name='login'),
    path('users/token/refresh/', views.VerifyUserView.as_view(), name='token_refresh'),
    path('category/<int:category_id>/story/new/', views.CategoryAddStoryDetail.as_view(), name='story-detail'),
    path('story/', views.StoryView.as_view(), name='story-index'),
    path('story/<int:story_id>/', views.StoryDetail.as_view(), name='story-detail'),
    path('story/<int:story_id>/review/new/', views.StoryAddReviewyDetail.as_view(), name='review-detail'),
    path('review/', views.ReviewView.as_view(), name='review-index'), 
    path('review/<int:review_id>/', views.ReviewDetail.as_view(), name='review-detail'),
]



    
