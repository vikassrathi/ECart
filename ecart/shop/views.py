import math

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact

# Create your views here.
def index(request):
    # Products=Product.objects.all()
    # n=len(Products)

    # params={'no_of_slides':nslides,'range':(1,nslides),'product':Products}
    allprods=[]
    catprods=Product.objects.values('category','id')
    # print(catprods)
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nslides = n // 4 + math.ceil((n / 4) + (n // 4))
        allprods.append([prod,range(1,nslides),nslides])
    # allprods=[[Products,range(1,len(Products)),nslides],[Products,range(1,len(Products)),nslides] ]
    params={'allprods':allprods}
    return render(request,'shop\index.html',params)



def about(request):
    return render(request,'shop\\about.html')


def contact(request):
    if request.method=='GET' or request.method == "POST":

        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
    # print(name)
    contact=Contact(name=name,email=email,phone=phone,desc=desc)
    contact.save()

    return render(request,'shop\\contact.html')

def tracker(request):
    return render(request,'shop\\tracker.html')

def search(request):
    return render(request,'shop\\search.html')


def productView(request,myid):
    products=Product.objects.filter(id=myid)


    return render(request,'shop\\prodView.html',{'product':products[0]})

def checkout(request):
    return render(request,'shop\\checkout.html')