from django.shortcuts import HttpResponse,render,redirect
from login.models import contact,booking,user
from login.models import feedback,comment
from package.models import package
from django.contrib import messages
def index(request):
    data=package.objects.all().values
    print(data)
    context={
        
        'item':data
    }
    request.session['user']=None
    return render(request,'index.html')

def login(request):
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact1(request):
    if request.method=="POST":
        contact1=contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message1=request.POST.get('Message')
        contact1.name=name
        contact1.email=email
        contact1.subject=subject
        contact1.message=message1
        a=contact1.save()
        print(a)
        messages.error(request,"Thanks For Contact US!!")


    return render(request,'contact.html')
    
def feedback1(request):
    print(request.session['id'])
    if not request.session['id']:
        messages.error(request,"Plzz Login First")
        return redirect('/')
    if request.method=="POST":
        feedback1=feedback()
        name=request.POST.get('name') 
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message1=request.POST.get('message')
        feedback1.name=name
        feedback1.email=email
        feedback1.subject=subject
        feedback1.message=message1
        feedback1.save()
        messages.error(request,"Your Message send Successfully....")

    return render(request,'feedback.html')

def tourpackage (request):
    return render (request,'tourpackage.html')

def destination (request):
    return render (request,'destination.html')

def travelguide (request):
    return render (request,'travelguide.html')

def booking1(request):

    if request.method=="POST":
        name=request.POST.get('name')
        price1=request.POST.get('price')
        inprise=int(price1)
        email=request.POST.get('email')
        phonenumber=request.POST.get('phone_no')
        adult=request.POST.get('adults')
        children=request.POST.get('children')
        checkindate=request.POST.get('checkindate')
        checkoutdate=request.POST.get('checkoutdate')
        totalperson=int(int(adult)+int(children))
        totalprice=totalperson*inprise
        packageid=request.POST.get('packageid')
        packagename=request.POST.get('packagename')
        print(name,email,phonenumber,adult,children,checkindate,checkoutdate,packageid,packagename)

        save=booking()
        save.name=name
        save.email=email
        save.phone_no=phonenumber
        save.adults=adult
        save.children=children
        save.checkindate=checkindate
        save.checkoutdate=checkoutdate
        save.packageid=packageid
        save.price=totalprice
        save.packagename=packagename
        save.save()
        return redirect('/profile')
    if request.method=="GET":
          data=user.objects.get(id=request.session['id'])
          id=request.GET.get('id')
          price=request.GET.get('prise')
         
          name=package.objects.get(id=id)
          print(name)
          print(id)
          context={
                'id':id,
                'price':price,  
                'name':name,
                'item':data
          }
    
        
    return render (request,'booking.html',context)



def bookingstatus (request):
    if request.method=="POST":
        id=request.POST.get('id')
        print(id)
        print("hello")
        data=booking.objects.get(id=id)
        context={
            'item':data
        }
        return render (request,'bookingstatus.html',context)

def packagedetails (request):
    if request.method=="POST":
        id=request.POST.get('id')
        print(id)
        data=package.objects.get(id=id)
        context={
            'item':data
        }
    return render (request,'packagedetails.html',context)

def profile (request):
    if request.method=="POST":
        name=request.POST.get('name')
        Email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        new=user.objects.get(id=request.session['id'])
        new.name=name
        new.email=Email
        new.phone=mobile
        new.save()

    data=user.objects.get(id=request.session['id'])
    print(data)
    data2=user.objects.filter(id=request.session['id']).values()
    email=data2[0].get('email')
    data3=booking.objects.filter(email=email)
    print(data3)
    context={
        'data':data3,

        'item':data
    }
    return render (request,'profile.html',context)

def comment1(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('massage')
        print(name,email,message)

        new=comment()
        new.FullName=name
        new.Email=email
        new.Message=message
        new.save()
        messages.error(request,"Message Send Successfully...!")
        
    return render (request,'comment.html')

def forget(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwordw=request.POST.get('password')
        print(passwordw)
        print(email)
        data=user.objects.get(email=email)
        if data:
            data.password=passwordw
            data.save()
            messages.error(request,"Password Reset Successfully")
            return redirect('login')
        else:
            messages.error(request,"User Does Not Exist")
    return render(request,'forgetpassword.html')