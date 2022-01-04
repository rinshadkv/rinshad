from django.shortcuts import render

# Create your views here.

def home(requast):
    return render(requast,'index.html')