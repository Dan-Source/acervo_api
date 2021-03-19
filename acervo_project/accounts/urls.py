from django.urls import path, include

from rest_framework import routers

from acervo_project.accounts import views

from rest_framework_simplejwt.views import TokenRefreshView
from acervo_project.accounts.views import (
    MyObtainTokenPairView,
    RegisterView,
    UserViewSet
)

app_name = 'accounts'

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
