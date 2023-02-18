"""
Database models
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

"""
1. define usermanager with base user manager default django class
2. define create user method
3. self.model will call User model class and create new object
4. set_password will set encrypted password using hashing mechanism
5. user.save will save the user object in the database
6. return user
"""
class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #assign user manager to custom user class
    objects = UserManager()

    # set default username field as email
    USERNAME_FIELD = 'email'