from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz_end/', views.quiz_end, name='quiz_end'),
    path('quiz_end_two/', views.quiz_end_two, name='quiz_end_two'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('doctor_dashboard/<str:doctor_id>/',
         views.doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/<str:id>/',
         views.patient_dashboard, name='patient_dashboard'),
    path('accept_patient/<str:id>/',
         views.accept_patient, name='accept_patient'),     

]



