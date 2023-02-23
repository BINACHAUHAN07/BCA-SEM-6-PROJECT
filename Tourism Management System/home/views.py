from django.shortcuts import render,HttpResponse
from package.models import *
# Create your views here.
def index(request):
    print("hello")
    data=package.objects.all()
    print(data)
    context={
        'item':data
    }
    return render(request,"index.html",context)
