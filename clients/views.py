# from django.http import HttpResponse
from django.shortcuts import render
from . models import Client
from .forms import CLientForm

# Create your views here.
# def home(request):
#     return render (request,"home.html")

def index(request):

    clients = Client.objects.all()
    context = {'clients':clients}
    return render (request,'clients/home.html',context)

def client(request,pk):
    client = Client.objects.get(id=pk)
    context = {'client':client}
    return render (request,'clients/client.html',context)

def createClient(request):
    form = CLientForm()
    context = { 'form':form }
    return render(request,'clients/client_form.html',context)