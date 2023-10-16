from django.db import models
from django.contrib.auth.models import User


class Medicine(models.Model):
    medicinename = models.CharField(max_length=100)
    expirydate = models.DateField()
    CATEGORY_CHOICES = (
        ('tablets','Tablets'),
        ('syrup','Syrup'),
    )
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    quantity = models.PositiveIntegerField() 
    def __str__(self):
        return self.medicinename
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class IssuedMedicine(models.Model):
    visit_number = models.CharField(max_length=100)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity_issued = models.PositiveIntegerField()
    issued_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Issued: {self.medicine.medicinename} - {self.quantity_issued} units on {self.issued_date}"
