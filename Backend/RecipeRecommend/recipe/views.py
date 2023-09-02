from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer , RecipeSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile , Recipe
import json , os , openai
from django.http import JsonResponse 

openai.api_key = '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'
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
@csrf_exempt
def register_user(request):
    """
    Register a new user.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        

        diet_preference = request.data.get('diet_preference')
        recipe_collection = request.data.get('recipe_collection')

        user_document = UserProfile(user=user,dietary_preferences=diet_preference,
            recipeCollections=recipe_collection)
        user_document.save()
        
        return Response({'msg':'user registered !'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    """
    Log in a user and retrieve a token.
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'msg':'Login succesfull','token': token.key}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_user_token(request):
    """
    Retrieve the token for the currently authenticated user.
    """
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_200_OK)

@csrf_exempt
def create_recipe(request):
    
    if request.method == 'POST':

        # Parse the JSON data from the request body
        data = json.loads(request.body)
        
        # Create a serializer with many=True to handle a list of recipes
        serializer = RecipeSerializer(data=data, many=True)
        
        if serializer.is_valid():
            # Save the recipes to the MongoDB database
            
            serializer.save()
            return JsonResponse({'message': 'Recipes created successfully'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
@api_view(['GET'])
def get_recipe(request):
    # Get all Recipe objects from the database
    recipes = Recipe.objects.all()

    # Serialize the queryset using your RecipeSerializer
    serializer = RecipeSerializer(recipes, many=True)

    # Return the serialized data as a JSON response
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])

def get_recipe_detail(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
        serializer = RecipeSerializer(recipe)  # Serialize the single recipe
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Recipe.DoesNotExist:
        return Response({'message': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)

@ csrf_exempt
def get_ai_suggestion(request):
    if request.method=='POST':
        data = json.loads(request.body)
        
        ingredients=data['ingredients_list']
        ingredients_not_required=data['not_ingredients_list']
        diet_prefrence=data['diet']

        placeholder_ingredients=','.join(f'ingredient {i}'for i in range(len(ingredients)))
        placeholder_not_ingredients=','.join(f'notingredient {i}'for i in range(len(ingredients_not_required)))
        
        prompt=f"give me the top three recipes which include ingredients {placeholder_ingredients} without {placeholder_not_ingredients} (you can suggest some other ingredient on the place of these, specifically mentioned what are the alternative ingredients and what are they alternative of ) and recipe should be {diet_prefrence}. Also give expected cooking time and number of serving can be done. Also give quantity along with ingredients. give one sentence description about dish. Do not give any introduction. or conclusions just give recipe."

        response=openai.Completion.create(
              model= "text-davinci-003",
              prompt= prompt,
             temperature= 1.2,
        )
       
        suggestions=response.choices[0].text.strip()

        return JsonResponse({'msg':suggestions})