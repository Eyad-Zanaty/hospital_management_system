from django.db import models
# Create your models here.

# nurses different specializations
specializations=(
    ('Critical Care', 'Critical Care'),
    ('Emergency', 'Emergency'),
    ('Oncology', 'Oncology'),
    ('Pediatrics', 'Pediatrics'),
    ('Geriatrics', 'Geriatrics'),
)

shifts= (
    ('morning', 'morning'),
    ('afternoon/evening', 'afternoon/evening'),
    ('night', 'night'),
)


class Nurse(models.Model):
    fullname= models.CharField(max_length= 255)
    department= models.CharField(max_length= 255, choices= specializations)
    phone_number= models.CharField(max_length= 255)
    shift_type= models.CharField(max_length= 255, choices= shifts)
    
    class Meta:
        ordering= ['id']
    
    def __str__(self):
        return f'{self.department} - {self.fullname}'