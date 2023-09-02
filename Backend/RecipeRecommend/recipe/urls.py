from django.urls import path
from . import views

urlpatterns = [
    path('api/register/', views.register_user, name='register-user'),
    path('api/login/', views.login_user, name='login-user'),
    path('api/get-token/', views.get_user_token, name='get-user-token'),
    path('api/add-recipe/', views.create_recipe, name='create-recipe'),
    path('api/get-recipe/' , views.get_recipe , name='get-recipe'),
    path('api/recipe-detail/<int:recipe_id>/', views.get_recipe_detail, name='get-recipe-details'),
    path('api/recipe-recommend/', views.get_ai_suggestion, name='get-recipe-recomm'),
]