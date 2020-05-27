from django.shortcuts import render

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

def profile(request):
    return render(request,'profile.html')

# Create your views here.
