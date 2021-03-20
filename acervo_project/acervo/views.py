from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Author, Category, Book, Acervo
from .serializers import (
    AuthorSerializer, 
    CategorySerializer, 
    BookSerializer, 
    AcervoSerializer
)


class AuthorViewSet(ModelViewSet):
    permission_classes = ['IsAuthenticated']
    serializer_class = AuthorSerializer()
    ordering = ('-created')


class CategoryViewSet(ModelViewSet):

    permission_classes = ['IsAuthenticated']
    serializer_class = CategorySerializer()
    ordering = ('-created')


class BookViewSet(ModelViewSet):
    permission_classes = ['IsAuthenticated']
    serializer_class = BookSerializer()
    ordering = ('-created')


class AcervoViewSet(ModelViewSet):
    permission_classes = ['IsAuthenticated']
    serializer_class = AcervoSerializer()
    ordering = ('-created')





