"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path函数具有四个参数，两个必选：route和view，两个可选：kwargs和name
    # route是类似正则表达式的准则，用于匹配url中的目录名
    # view 当django匹配到目录时，调用view视图函数
    # kwargs 关键字参数会作为字典传给目标视图函数
    # name 给当前url命名，以便引用
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
