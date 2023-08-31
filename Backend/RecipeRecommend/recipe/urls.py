from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register_user, name='register-user'),
    path('api/login/', views.login_user, name='login-user'),
    path('api/get-token/', views.get_user_token, name='get-user-token'),
]