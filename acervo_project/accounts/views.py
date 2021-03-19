from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import User
from .permissions import IsUserOwner

from acervo_project.accounts.serializers import (
    UserSerializer, 
    UpdateUserSerializer,
    RegisterSerializer,
    MyTokenObtainPairSerializer
)


class UserViewSet(ModelViewSet):
    permission_classes = ('IsAuthenticated')
    serializer_class = UserSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username')
        if self.request.user.is_superuser:
            return User.objects.all().order_by('created')
        if username:
            return User.objects.filter(username=username)
    
    def get_serializer_class(self):
        if self.action == 'update':
            return UpdateUserSerializer
        return UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all() # ver o uso dessa filtro aqui
    permission_classes = (AllowAny)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny)
    serializer_class = MyTokenObtainPairSerializer
