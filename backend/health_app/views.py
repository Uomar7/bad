from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from . models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def welcome(request):
    

    return render(request,'index.html')