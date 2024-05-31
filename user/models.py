import uuid 
from django.db import models
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManger

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    GENDER = {
        'm':'Male',
        'f':'Female',
        'x':'Prefer not to say'
    }
    user_id = models.UUIDField(
        primary_key = True, 
         default = uuid.uuid4, 
         editable = False
    )
    
    email = models.EmailField(unique=True,default='',blank=True)
    firstname = models.CharField(max_length=225,default='',blank=True)
    lastname = models.CharField(max_length=225,default='',blank=True)
    bio = models.TextField(max_length=225,default='',blank=True)
    sex = models.CharField(max_length=2,choices=GENDER,default='x')
    
    avatar = models.CharField(max_length=225,default='',blank=True,null=True)
    banner = models.CharField(max_length=225,default='',blank=True,null=True)
    status = models.CharField(max_length=225,default='',blank=True,null=True)
    online = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    login_login = models.DateTimeField(blank=True,null=True)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELD = []
    
    
    objects = UserManger()
    
    def get_full_name(self):
        return self.firstname + " " + self.lastname
    
    def get_short_name(self):
        return self.lastname or self.email.split('@')[0]
    
    def __str__(self) -> str:
        return self.email

    class META:
        verbose_name = 'User'
        verbose_name_plural = 'Users'