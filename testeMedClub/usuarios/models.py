import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
# Create your models here.
class usuario(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
     # Campos obrigatórios para compatibilidade com Django auth
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = [ 'nome','senha']
    USERNAME_FIELD = 'email'
    def __str__(self):
        return self.nome
    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True
    
    @property
    def id(self):
        return self.id_usuario