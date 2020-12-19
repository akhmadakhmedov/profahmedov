from django.db import models

# Create your models here.

class Contact(models.Model):
    Name_Surname = models.CharField(max_length=30)
    Phone_number = models.CharField(max_length=18)
    Subject = models.CharField(max_length=30)
    Message = models.TextField()

    def __str__(self):
        return self.Name_Surname
