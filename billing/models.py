from django.db import models

# Create your models here.

class Billing(models.Model):
    total= models.IntegerField()
    payment_method= models.CharField(max_length= 255,choices=(('Visa', 'Visa'), ('Cash', 'Cash')))
    payment_id= models.CharField(max_length= 255, blank= True, null= True)
    payment_status= models.CharField(max_length= 255, choices=(('Pending', 'Pending'), ('Done', 'Done')))
    invoice_date= models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return f"{self.invoice_date.strftime('%Y-%m-%d')} - {self.payment_method} - {self.payment_status}"