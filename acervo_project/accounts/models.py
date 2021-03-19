import re

from django.db import models
from django.contrib.auth.models import (
        AbstractUser, PermissionsMixin, UserManager
)
from django.core import validators


class User(AbstractUser, PermissionsMixin):

    username = models.CharField(
        'Usuário', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido. '
                'Este valor deve conter apenas letras, números '
                'e os caracteres: @/./+/-/_ .'
                , 'invalid'
            )
        ], help_text='Utilize um nome curto que será usado para identificá-lo'
    )
    email = models.EmailField('E-mail', blank=True, null=True)
    is_superuser = models.BooleanField('Superuser', default=False)
    created = models.DateTimeField('Criado', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'