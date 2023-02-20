"""
Views for the user API
"""

from rest_framework import generics

from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    # django sets relevant serializer to serializer_class
    serializer_class = UserSerializer