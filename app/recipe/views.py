"""
Views for recipe API
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet): # ModelViewSet specifically set up to work with a model. Auto supports all CRUD endpoints
    """View for manage recipe API endpoints"""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all() # specifiy which objects are avialable through this modelviewset
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the appropriate serialzer class for the request"""
        if self.action == 'list': # if action is list, user recipe serializer to return all recipes
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)




