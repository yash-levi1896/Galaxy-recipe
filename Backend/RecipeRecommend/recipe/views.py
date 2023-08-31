from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
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
