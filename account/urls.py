from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('alumniSheet/', views.alumniSheet, name='alumniSheet'),
    path('alumni_sheet/', views.alumni_sheet, name='alumni_sheet'),
]