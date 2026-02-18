from django.db import models

# Create your models here.

rooms_types=(
    ('Private Room', 'Private Room'),
    ('Semi-Private Rooms', 'Semi-Private Room'),
    ('Ward Room', 'Ward Room'),
    ('Suites/VIP Room', 'Suites/VIP Room'),
    ('Procedure/Treatment Room', 'Procedure/Treatment Room'),
)

class Room(models.Model):
    number= models.IntegerField()
    type= models.CharField(max_length= 255, choices= rooms_types)
    admission_date= models.DateTimeField()
    discharge_date= models.DateTimeField()
    nursing_progress_notes= models.TextField(max_length= 1500)
    total_bill= models.DecimalField(max_digits= 10, decimal_places= 2)
    
    class Meta:
        ordering= ['number']
    
    def __str__(self):
        return f'{self.number} - {self.type.strip().capitalize()}'    