from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager): # Custom user manager to handle user creation and superuser creation
    def create_user(self, first_name: str, last_name: str, email: str, password: str=None, is_staff= False, is_superuser=False, **extra_fields):
        
        if not email:
            raise ValueError('The Email field must be set')
        if not first_name:
            raise ValueError('The First Name field must be set')
        if not last_name:
            raise ValueError('The Last Name field must be set')
        
        
        user= self.model(first_name=first_name, last_name=last_name, email=self.normalize_email(email), is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.first_name= first_name
        user.last_name= last_name
        user.full_name= f'{first_name} {last_name}'
        user.set_password(password)
        user.is_active= True
        user.is_staff= is_staff
        user.is_superuser= is_superuser
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name: str, last_name: str, email: str, password: str=None, **extra_fields):
        user= self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields)
        
        user.save(using=self._db)
        return user



class User(AbstractUser): # Custom user model that extends AbstractUser and includes additional fields for hospital management system
    first_name= models.CharField(max_length=255)
    last_name=  models.CharField(max_length=255)
    email= models.EmailField(max_length=255, unique=True)
    role= models.CharField(choices=[('Admin', 'Admin'), ('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Receptionist', 'Receptionist')])
    phone_number= models.CharField(max_length=255)
    gender= models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')])
    date_of_birth= models.DateField(blank=True, null=True)
    address= models.CharField(max_length=255)
    employee_id= models.CharField(max_length=255, unique=True)
    job_title= models.CharField(max_length=255)
    data_joined= models.DateField(blank=True, null=True)
    shify_start_time= models.TimeField(blank=True, null=True)
    shift_end_time= models.TimeField(blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    
    FULL_NAME_FIELD = f'{first_name} {last_name}'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.role} - {self.first_name} {self.last_name}'


