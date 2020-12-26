import re

from django.shortcuts import render, redirect

# Create your views here.
#
from django.urls import reverse
from user.models import User


def register(request):
    """显示注册页面"""
    return render(request, 'df_user/register.html')

def register_handle(request):
    """进行注册处理"""
    # 接收数据
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')
    # 进行数据校验
    if not all([username, password, email]):
        return render(request, 'df_user/register.html', {'errmsg': '数据不完整'})

    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
        return render(request, 'df_user/register.html', {'errmsg': '邮箱格式不正确'})

    if allow != 'on':
        return render(request, 'df_user/register.html', {'errmsg': '请同意协议'})
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None
    if user:
        return render(request, 'df_user/register.html', {'errmsg': '用户名已存在'})


    # 进行业务处理：进行用户注册
    user = User.objects.create_user(username, email, password)
    user.is_active = 0
    user.save()
    # 返回应答,跳转至首页
    return redirect(reverse('goods:index'))
