from django.urls import path, include

from rest_framework import routers

from acervo_project.acervo import views


app_name = 'acervo'

router = routers.DefaultRouter()

router.register('author', views.AuthorViewSet, basename='acervo')
router.register('category', views.CategoryViewSet, basename='acervo')
router.register('book', views.BookViewSet, basename='acervo')
router.register('acervo', views.AcervoViewSet, basename='acervo')

urlpatterns = [
    path('', include(router.urls))
]

