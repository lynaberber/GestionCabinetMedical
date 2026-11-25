from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Doctor, Patient, Specialty


admin.site.register(User, UserAdmin)
admin.site.register(Specialty)


@admin.register(Doctor)
class DoctorAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Infos médecin', {'fields': ('license_number', 'phone', 'specialties')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Infos médecin', {'fields': ('license_number', 'phone', 'specialties')}),
    )


@admin.register(Patient)
class PatientAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Infos patient', {'fields': ('national_id', 'phone', 'birth_date')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Infos patient', {'fields': ('national_id', 'phone', 'birth_date')}),
    )