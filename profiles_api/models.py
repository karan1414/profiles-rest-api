from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models

from profiles_project import settings


# we create managers when we want to implement some costum functionalities in Django inbuilt code.
# The way managers work is we speficy some functions within the manager that can be used to manipulate objects within the model the manager is for
class UserProfileManager(BaseUserManager):
    """ MAnager for user profile """
    # In this case we are making the manager since we want to use email instead of username which is present in django by default.
    # this is what django will use to create function using command line tool.

    def create_user(self, email, name, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError("Users must have an email address!")

        email = self.normalize_email(email=email)
        # self.model is set to the model that the manager is for and then it will create new model object that will set the email and the name 
        user = self.model(email=email, name=name)
        # we use .set_password to store passwords as hash
        user.set_password(password)
        # specify the database we want to use, standard procedure to save obj in django
        user.save(using=self._db)

        return user 

    def create_superuser(self,email,name,password):
        """ New superuser with given details """
        user = self.create_user(email, name, password)

        # we can use is_superuser even if it is not specifically defined in the models like is_staff but it is available from PermissionsMixin
        user.is_superuser = True 
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):

    ''' Database model for users in system '''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # if they can have access to django admin
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrive full name of user """
        return self.name 
    
    def get_short_name(self):
        """ Retrive short name of user """  
        return self.name

    def __str__(self):
        """ Return string representation of user  """
        return self.email

class ProfileFeedItem(models.Model):
    """ Profile status updates """
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return model as string """
        return self.status_text


