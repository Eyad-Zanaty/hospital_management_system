from django.db import models

# Create your models here.

# tests categories
tests=(
    ('Hematology', 'Hematology'),
    ('Clinical Chemistry', 'Clinical Chemistry'),
    ('Immunology/Serology', 'Immunology/Serology'),
    ('Urinalysis', 'Urinalysis'),
    ('Toxicology', 'Toxicology'),
)

# units of measurement
units=(
    ('mg/dL', 'mg/dL'),
    ('mmol/L', 'mmol/L'),
    ('mEq/L', 'mEq/L'),
    ('µmol/L', 'µmol/L'),
    ('µU/mL', 'µU/mL'),
)

class Laboratory(models.Model):
    test_name= models.CharField(max_length=255)
    test_category= models.CharField(max_length=255, choices= tests)
    normal_range= models.DecimalField(max_digits=5, decimal_places=2)
    unit= models.CharField(max_length=255, choices=units)
    
    class Meta:
        ordering= ['id']
    
    def __str__(self):
        return f'{self.test_name.strip().capitalize()}'