from rest_framework import serializers
from .models import Author, Category, Book, Acervo
from acervo_project.accounts.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        ordering=['created']
        fields = ['id', 'name']
        extra_kwargs = {'id': {'read_only': True}}

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'nome', 'description']
        extra_kwargs = {'id': {'read_only': True}}

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        ordering = ['created']
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True}}

class AcervoSerializer(serializers.ModelSerializer):

    owner = UserSerializer
    # queryset = Book.objects.all()
    book = BookSerializer(many=True)

    class Meta:
        model = Acervo
        fields = ['owner', 'book']
        extra_kwargs = {'id': {'read_only': True}}
