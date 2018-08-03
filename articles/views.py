# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Articles
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def articlelist(request):
    #return HttpResponse("about")
    article=Articles.objects.all().order_by('date');
    #return HttpResponse("hello")
    return render(request,'articles/article.html',{'articles':article})
def articledetail(request,slug):
    #return HttpResponse(slug)
    article=Articles.objects.get(slug=slug)
    return render(request,'articles/articledetail.html',{'article':article})
@login_required (login_url='/accounts/login/')
def create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
            # validates wheter all fields came etc files is for images
        if form.is_valid():
            # validates whether all fields are corect are not
            #save db
            a=form.save(commit=False)
            a.author=request.user
            a.save()
            return redirect('articles:list')
    else:
        form=forms.CreateArticle()
        return render(request,'articles/create.html',{'form':form })
