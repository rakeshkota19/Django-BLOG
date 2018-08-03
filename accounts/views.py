# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def sign(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            #use to save form    form .save()
            user=form.save()
            login(request,user)
            return redirect('articles:create')
    else:
        form=UserCreationForm()
    return render(request,'accounts/sign.html',{'form':form})

    #return render(request,'accounts/sign.html')
def log(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in user
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})
def logoutview(request):
    if request.method=='POST':
        logout(request)
        return redirect('accounts:login')
