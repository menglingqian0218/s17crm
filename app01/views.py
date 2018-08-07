from django.shortcuts import render,HttpResponse,redirect
from django.forms import Form
from django.forms import fields
from django.forms import widgets
from rbac import models
from rbac.service.init_permission import init_permission



class LoginForm(Form):
    username = fields.CharField(required=True,error_messages={'required': "用户名不能为空"})
    password = fields.CharField(required=True,error_messages={'required': "密码不能为空"})

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,'login.html',{'form':form})
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # 用户名和密码通过验证
            # 1. 去数据库中检测用户是否存在
            user = models.UserInfo.objects.filter(**form.cleaned_data).first()
            if user:
                #role_list = user.roles.all()
                init_permission(request,user)
                return redirect('/index/')

            else:
                # 登录失败，主动提示错误
                # form.add_error("password", "用户名或密码错误")
                from django.core.exceptions import ValidationError
                form.add_error("password", ValidationError('用户名或密码错误'))
        return render(request, 'login.html', {'form': form})

import re
from django.conf import settings
def index(request):

    current_request_url = request.path_info

    permission_dict =request.session.get(settings.XX)
    if not permission_dict:
        return HttpResponse('未登录')
    flag = False
    for group_id,values in permission_dict.items():
        for url in values['urls']:
            regex = settings.URL_FORMAT.format(url)
            if re.match(regex,current_request_url):
                flag = True
                break
        if flag:
            break
    if not flag:
        return HttpResponse('无权访问')
    return HttpResponse('欢迎登陆')
def userinfo(request):
    return render(request, 'userinfo.html')

def userinfo_add(request):
    return render(request, 'userinfo_add.html')