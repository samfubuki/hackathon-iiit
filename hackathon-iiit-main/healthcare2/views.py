from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *


def home(request):
    return render(request, 'healthcare2/home.html')

def quiz(request):
    return render(request, 'healthcare2/quiz.html')

def quiz_end(request):
    return render(request, 'healthcare2/quiz_end.html')   

def quiz_end_two(request):
    return render(request, 'healthcare2/quiz_end_two.html')       

def registerPage(request):

    if request.method == 'POST':
        name = request.POST.get('name', '') 
        email = request.POST.get('email', '') 
        pass1 = request.POST.get('password1', '') 
        pass2 = request.POST.get('password2', '') 
        city = request.POST.get('city', '') 
        phone = request.POST.get('phone', '') 
        
        aduser = Aduser(name = name, email = email, createpass = pass1, confirmpass = pass2, city = city, phone = phone)
        aduser.save()
        return redirect('login')

    return render(request, 'healthcare2/register.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # if logged in user has arrived
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'healthcare2/login.html', context)


def doctor_dashboard(request, doctor_id):
    remaining = Patient.objects.all().filter(alloted = False).count()
    total = Patient.objects.all().filter(alloted = True).count()
    rem_patients = Patient.objects.all().filter(alloted = False)
    tot_patients = Patient.objects.all().filter(alloted=True)
    
    return render(request, 'healthcare2/doctor_dashboard.html', {'total':total, 'remaining':remaining, 'rem_patients':rem_patients, 'tot_patients':tot_patients}) 

def patient_dashboard(request, id):
    patient = Patient.objects.get(id=id)
    return render(request, 'healthcare2/patient_dashboard.html', {'patient':patient})
    
def accept_patient(request):
    pass

