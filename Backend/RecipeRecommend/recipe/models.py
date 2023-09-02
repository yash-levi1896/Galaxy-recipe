from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dietary_preferences = models.CharField(blank=True, max_length=100)
    recipeCollections=models.JSONField(default=list, blank=True)
    # Add other fields as needed

    # Define a method to get personalized recipe collections
    def get_recipe_collections(self):
        return self.recipeCollections.all()

    def __str__(self):
        return self.user.username
    
class Recipe(models.Model):
      image_url = models.URLField(max_length=200)  # Add the image URL field
      title = models.CharField(max_length=200)
      description = models.TextField()
      ingredients = models.JSONField(default=list,blank=True)  
      instructions = models.TextField(blank=True)
      cooking_time = models.PositiveIntegerField()  # In minutes
      servings = models.PositiveIntegerField()
      diet_preference=models.CharField(max_length=50 , default='vegan')

      def __str__(self):
        return self.title