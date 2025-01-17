from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)  # Corrected field name
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + " " + self.lname  # Added a space between fname and lname
