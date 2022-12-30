from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),

    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('alumniSheet/', views.alumniSheet, name='alumniSheet'),
    path('alumni_sheet/', views.alumni_sheet, name='alumni_sheet'),
    path('alumni_sheet/search/', views.search, name="search"),
    path('alumni_sheet/<slug:alumni_name>/', views.selected_name, name="selected name"),
]