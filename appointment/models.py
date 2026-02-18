from django.db import models

# Create your models here.

class Appointment(models.Model):
    date= models.DateField(verbose_name='Date')
    time= models.TimeField(verbose_name='Time')
    status= models.CharField(verbose_name='Status', choices=(('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')))
    patient_notification_status= models.BooleanField(verbose_name= 'Notification Status',default=False)
    reminder_time= models.DateTimeField(verbose_name='Reminder Time',null=True,blank=True)
    
    def __str__(self):
        return f"Appointment on {self.appointment_date} at {self.appointment_time}"