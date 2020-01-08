from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import HttpResponse
from web.models import User
from web import form as local_form


def index(request):
    user = request.session.get('user', False)
    return render(request, 'index.html', {'user': user})

#显示页面
def registerView(request):
    user = request.session.get('user', False)
    if not user:
        return render(request, 'login.html')
    else :
        return HttpResponseRedirect('/index/')


# 注册
def register(request):
    if request.method == 'POST':
        data = request.POST
        a = local_form.RegisterForm(data)
        if a.is_valid():
            if User.objects.filter(username=data['username']).exists():
                return render(request, 'immediate.html', {'registed': True, 'name': data['username']})
            user = User(**a.cleaned_data)
            user.save()
            return render(request, 'immediate.html', {'name': data['username']})
    return HttpResponseRedirect('/index/')


#登录
def login(request):
    user = request.POST.get('username', None)
    password = request.POST.get('password', None)
    result = User.objects.filter(username=user, password=password)
    if not result:
        return HttpResponse('用户名或者密码不正确')
    else:
       request.session['user'] = user
       #return HttpResponse('登录成功')
       return HttpResponseRedirect('/index/')
#注销
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')
#推荐算法

from web import engine
from web.models import movie,User
import random
def recommand1(request):#根据个人信息
    #获取用户出生日期
    uyear = User.objects.filter()
    #从Movie中获取相关年份电影
    mov = movie.objects.filter(myear=uyear)
    ran = random.randint(0,9)
    mov = mov[ran]
    return HttpResponse(mov.myear)

