#-*-coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,HttpResponsePermanentRedirect

def index(request):
    #return  HttpResponse('Hello')
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")

def login_action(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if username=='leo'and password=='123':
            #return HttpResponse('sucess')
            return HttpResponsePermanentRedirect('/event_manage/')
        else:
            return render(request,'login.html',{'error':'username or password error'})