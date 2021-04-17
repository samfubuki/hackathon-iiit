from django.db import models
from django.contrib.auth.models import User

class Aduser(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True)
    createpass = models.CharField(max_length=50, null=True)
    confirmpass = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=200, null=True)

    def __str(self):
        return self.id


class Doctor(models.Model):
    SPECIALITY_CHOICES = (
        ('Allergist', 'Allergist'),
        ('Immunologists', 'Immunologists'),
        ('Anesthesiologists', 'Anesthesiologists'),
        ('Cardiologists', 'Cardiologists'),
        ('Neurologists', 'Neurologists'),
        ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons'),
        ('Radiologists', 'Radiologists'),
        ('Physician', 'Physician')
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    speciality = models.CharField(
        max_length=50, null=True, blank=True, choices=SPECIALITY_CHOICES)
    availablity = models.BooleanField(default=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=50, null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    CHOICES = (
        ('Fever', 'Fever'),
        ('Body Ache', 'Body Ache'),
        ('Cold', 'Cold'),
        ('Cough', 'Cough'),
        ('Difficulty in Breathing', 'Difficulty in Breathing'),
        ('Loss in smell and taste', 'Loss in smell and taste'),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    symptoms = models.CharField(max_length=200, null=True, choices=CHOICES)
    severity = models.BooleanField(default=False)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=50)
    alloted = models.BooleanField(default=False)
    assigned_doctor = models.ForeignKey(Doctor, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL)
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    appointment_date = models.DateField(auto_now_add=True, null=True)
    appointment_time = models.TimeField(auto_now=True, auto_now_add=False)
    medicine = models.TextField(max_length=100, null=True, blank=False)
    diet = models.TextField(max_length=500, null=True, blank=False)

    def __str__(self):
        return self.doctor.name


