# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Hub import session

#login page
def index(request):

    #render login page
    if request.method == 'GET':
        return render(request, 'login/index.html')

    #create session and redirect to homepage
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print email
        print password

        session.user['email'] = email
        session.user['password'] = password

        s = session.getAmazonSession(session.user['email'], session.user['password'])
        session.s['session'] = session
        #todos need to valid login
        return redirect('home')

#home/hub page
def home(request):

    #render homepage
    if request.method == 'GET':
    return HttpResponse("cat")
