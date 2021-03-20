from django.db import models
from acervo_project.accounts.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ManyToManyField(
        Author, blank = True
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )
    cover = models.ImageField(upload_to='acervo/media', blank=True)
    year = models.IntegerField()
    description = models.TextField()
    num_pages = models.IntegerField(default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'


class Acervo(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    my_acervo = models.ManyToManyField(Book,  verbose_name='Acervo')

    def __str__(self):
        return '{self.name} Acervo'

    class Meta:
        verbose_name = 'Acervo'
        verbose_name_plural = 'Acervos'
