# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
import json
import os,sys, time
from subprocess import Popen,PIPE,check_output,STDOUT
import subprocess
from front.models import User

from django import forms


import sys
reload(sys)

sys.setdefaultencoding('utf-8')


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput)
    class_name = forms.CharField(label='班级名称')

def index(request):
    
    return render(request, 'index.html')


def test(request):
    value = request.COOKIES.get('username', "")
    if value:
        return render(request, 'test.html',{'username':value})
    else:
        return HttpResponseRedirect('/login')


def compile_code(request):
    res = dict()
    if request.method == 'POST':
        code = request.POST['code']
        exec_cmd = sys.executable
        if not os.path.isdir('tmp'):
            os.mkdir('tmp')
        username = request.COOKIES.get('username', '')
        file_name = username + '_' + str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())))
        file_path = "tmp/" + file_name + ".py"
        with open(file_path, 'w') as f:
            f.write(code)

        try:
            out_data = decode(check_output([exec_cmd, file_path], stderr=STDOUT))

        except subprocess.CalledProcessError as e:
            res["code"] = '1'
            res["output"] = decode(e.output)

        else:

            res['output'] = out_data
            res["code"] = 0

        finally:

            try:
                """
                os.remove(file_path)
                """
            except Exception as e :
                exit(1)

        return HttpResponse(json.dumps(res), content_type="application/json")


def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')


def register(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            class_name = user_form.cleaned_data['class_name']

            User.objects.create(username=username,password=password, class_name=class_name)

            response = HttpResponseRedirect('/test', {'user_form': user_form})
            response.set_cookie('username', username, 3600)
            return response

    else:
        user_form = UserForm()
    return render(request, 'register.html',{'user_form':user_form})


def login(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']

            user = User.objects.filter(username__exact=username,password__exact=password)

            if user:
                response = HttpResponseRedirect('/test')
                response.set_cookie('username',username, 3600)
                return response
            else:
                return HttpResponse('用户名或密码错误,请重新<a href="/login">登录</a>')



    else:
        user_form = UserForm()
    return render(request, 'login.html',{'user_form':user_form})


def logout(request):
    # 清理cookie里保存username
    response = HttpResponseRedirect('/login')
    response.delete_cookie('username')
    return response