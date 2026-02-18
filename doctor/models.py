from django.db import models

# Create your models here.

days=(
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday')
)

# doctors specializations
specializations=((
    ('Internists', 'Internists'),
    ('Nephrologists', 'Nephrologists'),
    ('Osteopaths', 'Osteopaths'),
    ('Pathologists', 'Pathologists'),
))

class Doctor(models.Model):
    fullname= models.CharField(max_length=255)
    specialization= models.CharField(max_length=255, choices= specializations)
    license_number= models.IntegerField()
    phone_number= models.CharField()
    email= models.EmailField()
    working_days= models.CharField(choices=days)
    consultation_fee= models.IntegerField()
    
    class Meta:
        ordering= ['id']
    
    def __str__(self):
        return f'{self.specialization} - {self.fullname.strip().capitalize()}'