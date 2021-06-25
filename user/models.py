from django.db import models
from django.contrib.auth.models import AbstractBaseUser,\
    BaseUserManager, PermissionsMixin


# Customize UserManager Class
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and Save a New User"""
        if not email:
            raise ValueError("You must inpul valid email")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        # Set encrypted password
        user.set_password(password)
        # (using = self._db ) multiple database  
        user.save(using=self._db)        
        return user 

    def create_superuser(self, email, password):
        """Create super User and save new one"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Customize User model class
class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Models That Will Help Us using Email as username"""
    email = models.EmailField(max_length=300, unique=True)
    name = models.CharField(max_length=300)
    username = models.CharField(max_length=300,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    # Make email as username field
    USERNAME_FIELD = 'email'
