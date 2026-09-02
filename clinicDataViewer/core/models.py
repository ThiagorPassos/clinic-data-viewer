import uuid
from django.db import models
from django.contrib.auth.models import User

class ClinicalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clinical_profile')
    emergency_phone = models.CharField(max_length=20, blank=True, null=True)
    blood_type = models.CharField(max_length=3, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    illnesses = models.TextField(blank=True, null=True)
    surgeries = models.TextField(blank=True, null=True)
    pin_code = models.CharField(max_length=4)
    qr_code_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Perfil Clínico - {self.user.username}"
