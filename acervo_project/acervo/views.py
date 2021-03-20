from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import(
    Author,
    Category,
    Book,
    Acervo
)

from .serializers import(
    AuthorSerializer, 
    CategorySerializer, 
    BookSerializer, 
    AcervoSerializer
)


class AuthorViewSet(ModelViewSet):

    permission_classes = ['IsAuthenticated']
    serializer_class = AuthorSerializer()
    queryset = Author.objects.all()


class CategoryViewSet(ModelViewSet):

    permission_classes = ['IsAuthenticated']
    serializer_class = CategorySerializer()
    queryset = Category.objects.all()



class BookViewSet(ModelViewSet):
    permission_classes = ['IsAuthenticated']
    serializer_class = BookSerializer()
    queryset = Book.objects.all()


class AcervoViewSet(ModelViewSet):
    permission_classes = ['IsAuthenticated']
    serializer_class = AcervoSerializer()
    queryset = Acervo.objects.all()





