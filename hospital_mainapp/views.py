from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    return render(request, 'hospital_mainapp/home.html')

def index(request):

    return render(request, 'hospital_mainapp/index.html')

def queue(request):

    return render(request, 'hospital_mainapp/queue.html')