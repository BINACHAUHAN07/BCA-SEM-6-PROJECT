from django.shortcuts import render
from .models import package

# Create your views here.
def package1(request):
    data=package.objects.all()
    context={
        'item':data
    }
    print(data)
    return render(request,'tourpackage.html',context)
