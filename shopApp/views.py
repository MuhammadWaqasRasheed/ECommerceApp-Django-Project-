from django.shortcuts import render
from .models import Brand,Laptop
# Create your views here.
def home(request):
    #getting Categories From DataBase
    brand=Brand.objects.all().order_by('name')
    laptops=Laptop.objects.all().order_by('price')
    params={'categories':brand , 'laptops':laptops}
    template='shopApp/home.html'
    return render(request,template,params)

def aboutUs(request):
    params={}
    template='shopApp/aboutUs.html'
    return render(request,template,params)

def contactUs(request):
    params={}
    template='shopApp/contactUs.html'
    return render(request,template,params)