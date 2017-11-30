# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# 引入我们创建的表单类
from .form import AddForm

# Create your views here.


def index(request):
    if request.method == 'POST':  # 当提交表单时
        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:  # 正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))
