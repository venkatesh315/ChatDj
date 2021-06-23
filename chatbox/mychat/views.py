from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from mychat.forms import EditPofileForm, CaptchaUserCreationForm
from django.contrib.auth import update_session_auth_hash
from mychat.search import search_user
def welcome(request):
    return render(request,'mychat/welcome.html')

def register(request):
    if request.method == 'POST':
        form = CaptchaUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')

            return redirect(register)
    else:
        form = CaptchaUserCreationForm()
    return render(request, "register/register.html", {'form': form})


def view_profile(request):

    args = {'user': request.user}
    return render(request, 'register/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditPofileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
         form=EditPofileForm(instance=request.user)
         args={'form':form}
         return render(request,'register/edit_profile.html',args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('view_profile')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'register/change_pwd.html', args)

def search_option(request):

    prof_users=User.objects.all()
    myFilter=search_user(request.GET, queryset = prof_users)
    prof_users=myFilter.qs
    return render(request, 'register/searching_user.html', {'all': prof_users,'user_form': myFilter})


