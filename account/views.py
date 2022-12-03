
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# from PIL import Image
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages

from .models import AlumniSheet


# Create your views here.

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User Created!!! ')
            # msg = 'user created'
            return redirect('login_view')
        else:
            # msg = 'form is not valid'
            messages.info(request, 'Username OR Password is incorrect')
    else:
        form = SignUpForm()
    return render(request,'Authentication/sign-up.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            varsityEmail = form.cleaned_data.get('varsityEmail')
            password = form.cleaned_data.get('password')
            user = authenticate(username=varsityEmail, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You login successfully!!! ')
                return redirect('index')

        else:
            # msg = 'error validating form'
            messages.info(request, 'error validating form')
    return render(request, 'Authentication/sign-in.html', {'form': form, 'msg': msg})






def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def alumniSheet(request):
    return render(request, 'alumni-sheet.html')

def alumni_sheet(request):
    sheet = AlumniSheet.objects.all()
    context = {
        'sheets': sheet
    }

    return render(request, 'alumni_sheet.html', context)

def selected_name(request, alumni_name):
    selected_name = AlumniSheet.objects.get(slug=alumni_name)
    return render(request, "single_alumni.html", {'selected_name': selected_name})

def search(request):
    alumni = request.GET['query']
    selected_name = AlumniSheet.objects.get(name=alumni)
    return render(request, "alumni_sheet.html", {'selected_name': selected_name})
