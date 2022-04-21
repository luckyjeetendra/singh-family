from django.db import models

# Create your models here.

class FamilyMember(models.Model):
    """docstring for FamilyMember"""

    name = models.CharField(max_length=200)
    mobile_number =  models.CharField(max_length=17, blank=True, null= True, help_text='Please enter correct number.')
    email = models.EmailField(max_length=70, blank=True, null= True, unique= True)
    address = models.TextField(blank=True, null= True, max_length=200)

    def __str__(self):
        return self.name
        