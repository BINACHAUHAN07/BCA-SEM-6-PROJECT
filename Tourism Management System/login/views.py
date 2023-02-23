from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mn=request.POST.get('phone')
        destination=request.POST.get('destination')
        pwd=request.POST.get('paasword')
        cpwd=request.POST.get('conformpaasword')
        print(name)
        print(email)
        print(mn)
        print(destination)
        print(pwd)
        fatch=user.objects.filter(email=email)
        print(fatch)
        if not len(pwd)<8:
            if not fatch:
                if not pwd==cpwd:
                    messages.error(request,"Password and Conform password is not correct!")
        
                else:
                    new=user()
                    new.name=name
                    new.phone=mn
                    new.destination=destination
                    new.password=pwd
                    new.email=email
                    new.save()
                    messages.error(request,"Register Successfully!!")
                    return redirect('login')
            else:
                messages.error(request,"User Already Exist !!")
        else:
            messages.error(request,"Password Must 8 Character Long ")   
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
       emai=request.POST.get('Email') 
       pwd=request.POST.get('Password')
       if user.objects.filter(email=emai).values():
          fatch=user.objects.filter(email=emai)
          passw=fatch[0].password
          if pwd==passw:
           print(fatch[0].id)
           request.session['id']=fatch[0].id
           print(request.session['id'])
           messages.error(request,"Login Successfully!!")
           return redirect('/')
          else:
           messages.error(request,"Password is Incorrect")
       else:
            messages.error(request,"User Does Not Exist")

    return render(request,'login.html')



def logout(request):
    request.session['id']=""
    messages.error(request,"Logout Successfull")
    return redirect('/')
    