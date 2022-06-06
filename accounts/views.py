from django.shortcuts import render

from rest_framework import viewsets
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated
from django.http import JsonResponse
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

def validate_username(request):
    
    username = request.GET.get('username', None)
    response = {
        'is_taken': CustomUser.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)
