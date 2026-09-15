from django import forms
from .models import ClinicalProfile

class ClinicalProfileForm(forms.ModelForm):
    pin_code = forms.CharField(min_length=4, max_length=4)

    class Meta:
        model = ClinicalProfile
        fields = ['full_name', 'emergency_phone', 'blood_type', 'allergies', 'medicines', 'illnesses', 'surgeries', 'pin_code']
