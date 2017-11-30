from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'TutorialList': TutorialList})
    #return render(request, 'home.html', {'string': string})
    #return render(request, 'home.html')


def test1(request):
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render(request, 'test1.html', {'info_dict': info_dict})


def test2(request):
    List = map(str,range(100))#长度为100的list
    return render(request, 'test2.html',{'List': List})

def add(request, a, b):
    c =  int(a) + int(b)
    return HttpResponse(str(c))

def test3(request,a):
    c = int(a)
    return render(request, 'test3.html', {'score': c})

