from django.contrib import admin
from django.urls import path, include
from .views import Home, CreateUserView, LoginView, VerifyUserView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('users/signup/', CreateUserView.as_view(), name='signup'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
]



    
