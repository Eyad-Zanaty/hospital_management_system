from django.db import models

# Create your models here.

genders=(
    ('male', 'male'),
    ('female', 'female'),
)

class Patient(models.Model):
    fullname= models.CharField(max_length= 255)
    phone= models.CharField(max_length= 255)
    gender= models.CharField(max_length= 255, choices=genders)
    
    class Meta:
        ordering= ['id']
    
    def __str__(self):
        return f'{self.fullname.strip().capitalize()}'