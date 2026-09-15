from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ClinicalProfile

@admin.register(ClinicalProfile)
class ClinicalProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_type', 'emergency_phone')
    search_fields = ('user__username', 'blood_type')
