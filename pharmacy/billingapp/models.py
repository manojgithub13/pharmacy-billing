from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

