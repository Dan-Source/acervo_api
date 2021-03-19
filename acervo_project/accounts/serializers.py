from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from acervo_project.accounts.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ordering=['created']
        fields = [
            'id', 'username'
        ]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username',  'email', 'password', 'password2')
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Os campos de senhas não são iguais."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.is_superuser = False        
        user.set_password(validated_data['password'])
        user.save()

        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        ordering = ['created']
        fields = [
            'id', 'username', 'email'
        ]
        extra_kwargs = {'id': {'read_only': True}}
