from django.shortcuts import render
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
import os


from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer



@api_view(['GET'])
def recent_matches(request):
    api_key = os.getenv('API_KEY')
    if not api_key:
        return Response({'error': 'No API key set'})
    
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return Response(data)  # Returns JSON from API
    else:
        return Response({'error': 'Failed to fetch data'})