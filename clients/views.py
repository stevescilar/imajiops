# from django.http import HttpResponse
from django.shortcuts import render
from . models import Client

# Create your views here.
# def home(request):
#     return render (request,"home.html")

def index(request):

    client = Client.objects.all()
    context = {'client':client}
    return render (request,'home.html',context)