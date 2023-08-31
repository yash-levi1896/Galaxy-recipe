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