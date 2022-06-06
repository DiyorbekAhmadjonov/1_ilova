from .views import CustomUserViewSet,validate_username

from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', CustomUserViewSet,basename="users")

urlpatterns = [
    path('', include(router.urls)), 
    path('validate_username/', validate_username, name='validate_username'),
    
]