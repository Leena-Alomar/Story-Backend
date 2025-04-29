from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('users/signup/', viewsCreateUserView.as_view(), name='signup'),
    path('users/login/', viewsLoginView.as_view(), name='login'),
    path('users/token/refresh/', viewsVerifyUserView.as_view(), name='token_refresh'),
    path('users/login/', viewsLoginView.as_view(), name='login'),
]



    
