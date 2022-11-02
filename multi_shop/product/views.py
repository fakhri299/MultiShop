from django.shortcuts import render
from product.models import *


    


def shop(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,'shop.html',context)

def detail(request,id):
    product=Product.objects.get(id=id)
    context={'product':product}
    return render(request,'detail.html',context)