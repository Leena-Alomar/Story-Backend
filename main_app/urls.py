from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('categories/', views.CategoryIndexView.as_view(), name='category-index'),
    path('users/signup/', views.CreateUserView.as_view(), name='signup'),
    path('users/login/', views.LoginView.as_view(), name='login'),
    path('users/token/refresh/', views.VerifyUserView.as_view(), name='token_refresh'),
    path('category/<int:category_id>/story/new/', views.CategoryAddStoryDetail.as_view(), name='story-detail'),
]



    
