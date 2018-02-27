# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
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

        session.user['email'] = email
        session.user['password'] = password

        s = session.getAmazonSession(session.user['email'], session.user['password'])

        #check if response return correct page since 200 status code still returnn
        #for correct and incorrect email/password
        BSObj = BeautifulSoup(s.text, 'lxml')
        createAccountSubmitId = BSObj.find(id="createAccountSubmit")
        if createAccountSubmitId:
            print True
            return render(request, 'login/index.html', {'error': 'email or password is incorrect'})
        else:
            return HttpResponse(s.text)

#home/hub page
def home(request):

    #render homepage
    if request.method == 'GET':
        return HttpResponse("cat")
