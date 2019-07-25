from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from . models import Profile
from .forms import NewProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/accounts/login/')
def welcome(request):
    

    return render(request,'index.html')
@login_required(login_url='/accounts/login/')      
def new_profile(request,id):
    user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
        return redirect('profile')
    else:
        form = NewProfileForm()
    return render(request, 'new-profile.html', {"form":form,"user":user})
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    
    return render(request, 'profile-page.html',{"profile":profile})