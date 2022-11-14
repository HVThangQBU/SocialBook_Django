from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth,User

def index(request):
  return render(request, 'index.html')

def signup(request):
 if request.method == 'POST':
   username = request.POST['username']
   email = request.POST['email']
   password = request.POST['password']
   password2 = request.POST['password2']
   if password == password2:
     if User.objects.filter(email=email).exists():
       messages.info(request,'EMAIL TAKENS')
       return redirect('signup')
     elif User.objects.filter(username=username).exists():
       messages.info(request,'USERNAME TAKENS')
       return redirect('signup')
     else:
       user = User.objects.create_user(username=username, email=email, password=password)
       user.save()
       # log user in and redirectto setting page
       # create a profile object for the new user
       user_model = User.objects.get(username=username)
     return redirect('index')
   else:
    messages.info(request,'PASS NOT MATCHING')
    return redirect('signup')

 else:
  return render(request, 'signup.html')
