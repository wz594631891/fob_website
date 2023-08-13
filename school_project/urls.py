# from django.views.static import serve #加载本地图片0308

"""school_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.views.generic.base import RedirectView#图标
from django.contrib.staticfiles.views import serve  #图标 

from django.contrib import admin
from django.urls import path
from web import views
urlpatterns = [
	path('contacts/',views.contacts),#路径函数对应关系,首页
	path('promotion/',views.promotion),#路径函数对应关系,首页
	path('profile/',views.profile),#路径函数对应关系,首页
	path('index/',views.index),#路径函数对应关系,首页
    path('admin/', admin.site.urls),
    path('search/',views.search),#福步搜索产品页
    path('product/',views.product),#福步产品页
    
    path('profile/',views.profile),#福步介绍页

    path('favicon.ico', serve, {'path': 'img/favicon.ico'}),  #图标 
    # #加载本地图片X
    # url(r'^book/(?P<path>.*)$', serve, {'document_root':'D:/github_goods'})
]
