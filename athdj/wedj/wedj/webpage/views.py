from django.shortcuts import render 
from django.http import HttpResponse
from . models import people

# Create your views here.
def home(request):
    peo=people.objects.all()


    
    return render(request,'index.html',{'peo':peo})