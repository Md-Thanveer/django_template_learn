from django.shortcuts import render


def home(request):
    return render(request, 'frontend/home.html')
def about(request):
    return render(request, 'frontend/about.html')

def services(request):
    return render(request, 'frontend/services.html')

def contact(request):
    return render(request, 'frontend/contact.html')
