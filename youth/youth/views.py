from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
#make function
def homePage(request):
     return render(request, "index.html")
def about(request):
     return render(request,"about.html")
def services(request):
     return render(request,"services.html")
def causes(request):
     return render(request,"causes.html")
def contact(request):
     return render(request,"contact.html")