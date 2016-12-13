#-*-coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,HttpResponsePermanentRedirect

def index(request):
    username=request.session.get('user','')
    return render(request,"index.html",{'user':username}) #返回页面


def login(request):
    return render(request,"login.html")

def login_action(request):
    if request.method == 'POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        if username=='leo'and password=='123':
            #return HttpResponse('sucess')
            response= HttpResponsePermanentRedirect('/index/')#跳转到主页
            request.session['user']=username #添加浏览器cookie
            return response

        else:
            return render(request,'login.html',{'error':'username or password error'})