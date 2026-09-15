import uuid
from django.db import models
from django.contrib.auth.models import User

class ClinicalProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, blank=True, null=True)
    medicines = models.TextField(blank=True, null=True)
    emergency_phone = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=5)
    allergies = models.TextField(blank=True, null=True)
    illnesses = models.TextField(blank=True, null=True)
    surgeries = models.TextField(blank=True, null=True)
    pin_code = models.CharField(max_length=4)

    def __str__(self):
        return f"Perfil Clínico - {self.user.username}"
