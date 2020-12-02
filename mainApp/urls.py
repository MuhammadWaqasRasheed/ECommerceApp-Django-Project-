"""mainApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

#imports for Shop
from shopApp import views as shopViews

urlpatterns = [
    path('admin/', admin.site.urls),
    #shopApp Paths
    path('',shopViews.home,name="shopHome"),
    path('shop/aboutUs',shopViews.aboutUs,name="shopAboutUs"),
    path('shop/contactUs',shopViews.contactUs,name="shopContactUs"),
]
