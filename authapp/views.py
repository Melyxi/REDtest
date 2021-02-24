from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from authapp.forms import UserForm, RegisterForm
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from authapp.models import User
from authapp.forms import *


def login(request):

    login_form = UserForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))

    content = {'login_form': login_form}
    return render(request, 'authapp/login.html', content)

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = RegisterForm()

    content = {'register_form': register_form}
    return render(request, 'authapp/register.html', content)




def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def edit(request):
    if request.method == "POST":
        edit_form = EditFormUser(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('main:user'))
    else:
        edit_form = EditFormUser(instance=request.user)

    content = {'form': edit_form}
    return render(request, 'authapp/edit.html', content)



