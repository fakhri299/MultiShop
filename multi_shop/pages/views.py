from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView

from product.models import Product
from .forms import ContactForm
from product.models import Category
# Create your views here.

# Create your views here.
def home(request):
    categories=Category.objects.all()
    recent_products=Product.objects.all().order_by()[:20]

    context={"categories":categories,
              "recent_products":recent_products}

    return render(request,'index.html',context)


def navbar_operations(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'partials/navbar.html',context)

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')





class ContactView(SuccessMessageMixin,FormView):
    template_name='contact.html'
    form_class= ContactForm
    success_url=reverse_lazy('contact')
    success_message='We recieved your request'
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
