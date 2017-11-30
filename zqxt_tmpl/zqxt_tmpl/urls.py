"""zqxt_tmpl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', learn_views.home, name='home'),  # new
    url(r'^test1/$', learn_views.test1, name='test1'),  # 注意修改了这一行
    url(r'^test2/$', learn_views.test2, name='test2'),  # 注意修改了这一行
    url(r'^test3/(\d+)/$', learn_views.test3, name='test3'),  # 注意修改了这一行
    url(r'^add/(\d+)/(\d+)/$', learn_views.add, name='add'),
]
