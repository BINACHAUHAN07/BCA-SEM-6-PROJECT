from django.db import models

class user(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    password=models.CharField(max_length=225)

    def __str__(self):
         return self.name


class contact(models.Model):
    name=models.CharField(max_length=50),
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
    def __str__(self):
        return self.email  



class feedback(models.Model):
    name=models.CharField(max_length=50),
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
     
     
          

class booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=50)
    adults=models.CharField(max_length=50)
    children=models.CharField(max_length=50)
    checkindate=models.CharField(max_length=50)
    checkoutdate=models.CharField(max_length=50)
    packageid=models.CharField(max_length=50)
    price=models.CharField(max_length=225)
    packagename=models.CharField(max_length=50)
    
    

    def __str__(self):
        return self.name

 
class comment(models.Model):
    FullName=models.CharField(max_length=250)
    Email=models.EmailField(max_length=250)
    Message=models.CharField(max_length=250)
    
    def __str__(self):
        return self.FullName 



  