from django.shortcuts import render

# Create your views here.
def home(request):
    params={}
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