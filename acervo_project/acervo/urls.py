from django.urls import path, include

from rest_framework import routers

from acervo_project.acervo import views


app_name = 'acervo'

router = routers.DefaultRouter()

router.register('author', views.AuthorViewSet, basename='user-author')
router.register('category', views.CategoryViewSet, basename='user-category')
router.register('book', views.BookViewSet, basename='user-book')
router.register('acervo', views.AcervoViewSet, basename='user-acervo')

urlpatterns = [
    path('', include(router.urls))
]

