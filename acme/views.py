from django.shortcuts import render

def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')

def handler404(request,exception=None):
    return render(request,'errors/404.html', status=404)

def handler500(request,exception=None):
    return render(request,'errors/500.html', status=500)