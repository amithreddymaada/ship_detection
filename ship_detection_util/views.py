from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request,'ship_detection_util/index.html', {"title":"Ship DD"})