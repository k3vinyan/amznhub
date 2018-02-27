# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from Hub import Session

#login page
def index(request):

    #render login page
    if request.method == 'GET':
        return render(request, 'login/index.html')

    #create session and redirect to homepage
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        s = Session.getAmazonSession(email, password)

        if Session.isAuthSession():
            return redirect('home')
        else:
            return render(request, 'login/index.html', {'error': 'email or password is incorrect'})


#home/hub page
def home(request):

    if request.method == 'GET':
        if Session.isAuthSession():
            return render(request, 'login/home.html')
        else:
            return redirect('index')
