from django.shortcuts import render,get_object_or_404
from product.models import *


    


def shop(request):
    products=Product.objects.all()
    colors=Color.objects.all()
    sizes=Size.objects.all()
    context={'products':products,'colors':colors,'sizes':sizes,}
    return render(request,'shop.html',context)

def detail(request,product_id):
    sizes=Size.objects.all() 
    colors=Color.objects.all()
    
    product=Product.objects.get(id=product_id)
   
    context={'product':product,'sizes':sizes,'colors':colors}
    
    return render(request,'detail.html',context)