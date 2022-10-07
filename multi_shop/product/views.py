from django.shortcuts import render
from product.models import Color
from product.models import Product

def all_products(request):
    all_products=Product.objects.all()

    context={'all_products':all_products}

    return render(request,'shop.html',context)


def detail_product(request,product_id):

    product=Product.objects.get(id=product_id)
    color=Color.objects.all()

    context={'product':product,'colors':color}

    return render(request,'detail.html',context)