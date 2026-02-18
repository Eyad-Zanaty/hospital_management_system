from django.db import models
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator

# Create your models here.

medicine_categories=(
    ('analgesics', 'analgesics'),
    ('antibiotics', 'antibiotics'),
    ('cardiovascular agents', 'cardiovascular agents'),
    ('antidepressants', 'antidepressants'),
    ('antidiabetics', 'antidiabetics'),
)

# medicine effect strength
strength_levels=(
    ('Low Strength', 'Low Strength'),
    ('Extra Strength', 'Extra Strength'),
    ('Double Strength', 'Double Strength'),
)

# forms of medicine
dosage_forms= (
    ('Tablets', 'Tablets'),
    ('Capsules','Capsules'),
    ('Cream','Cream'),
    ('Ointment','Ointment'),
    ('Eye Drops','Eye Drops'),
)

# most facmous medicine manufacturers
manufacturers= (
    ('Merck & Co', 'Merck & Co'),
    ('Pfizer', 'Pfizer'),
    ('AbbVie', 'AbbVie'),
    ('AstraZeneca', 'AstraZeneca'),
)

class Medicine(models.Model):
    fullname= models.CharField(max_length= 255)
    category= models.CharField(max_length= 255, choices= medicine_categories)
    strength= models.CharField(max_length= 255, choices= strength_levels)
    dosage_form= models.CharField(max_length= 255, choices= dosage_forms)
    quantity= models.DecimalField(max_digits= 5, decimal_places= 2)
    unit_price=  models.DecimalField(max_digits= 8, decimal_places=2)
    reorder_level= models.DecimalField(max_digits= 8, decimal_places=2)
    expiry_date= models.DateField(validators=[MinValueValidator(datetime.today)])
    manufacturer= models.CharField(max_length= 255, choices= manufacturers)
    
    class Meta:
        ordering= ['fullname']
    
    def __str__(self):
        return f'{self.fullname.strip().capitalize()}'