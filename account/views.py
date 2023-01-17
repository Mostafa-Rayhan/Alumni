
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# from .forms import SignUpForm, LoginForm
# from django.contrib.auth import authenticate, login, update_session_auth_hash
# from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages, auth
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from .models import AlumniSheet, Gallery


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        # linkedin = request.POST['linkedin']
        # varsity_id = request.POST['varsity_id']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Email is exist ')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username,  password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                messages.info(request, 'User Create Successfully !!!')
                # print("success")
                return redirect('login_view')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        print("no post method")
        return render(request, 'Authentication/register.html')






    # if request.method == 'POST':
    #     email = request.POST['email']
    #     v_id = request.POST['v_id']
    #     linkedin = request.POST['linkedin']
    #     password = request.POST['password']
    #     confirm_password = request.POST['confirm_password']
    #     if password == confirm_password:
    #         if AlumniUser.objects.filter(email=email).exists():
    #             messages.info(request, 'Email is exist ')
    #             return redirect(register)
    #         else:
    #             user = AlumniUser.objects.create_user(email=email, v_id=v_id, linkedin=linkedin, password=password)
    #             user.set_password(password)
    #             user.save()
    #             print("success")
    #             return redirect('login_view')
    #     else:
    #         messages.info(request, 'Both passwords are not matching')
    #         return redirect(register)
    # else:
    #     print("no post method")
    #     return render(request, 'Authentication/sign-in.html')


    # msg = None
    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         messages.success(request, 'User Created!!! ' + user)
    #
    #         return redirect('login_view')
    #     else:
    #         messages.info(request, 'Username OR Password is incorrect')
    # else:
    #     form = SignUpForm()
    # return render(request, 'Authentication/sign-up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_view')
    else:
        return render(request, 'Authentication/sign-in.html')






    # form = LoginForm(request.POST or None)
    # msg = None
    # if request.method == 'POST':
    #     if form.is_valid():
    #         varsityEmail = form.cleaned_data.get('varsityEmail')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=varsityEmail, password=password)
    #         if user is not None:
    #             login(request, user)
    #             messages.success(request, 'You login successfully!!! ')
    #             return redirect('index')
    #
    #     else:
    #         # msg = 'error validating form'
    #         messages.info(request, 'error validating form')
    # return render(request, 'Authentication/sign-in.html', {'form': form, 'msg': msg})






def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')

def gallery(request):
    img_list = Gallery.objects.all()
    context = {
        'lists': img_list
    }
    return render(request, 'gallery.html', context)

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
    if request.method == 'GET':
        alumni = request.GET.get['query']
        selected_name = AlumniSheet.objects.all().filter(name=alumni)
        return render(request, "alumni_sheet.html", {'selected_name': selected_name})
