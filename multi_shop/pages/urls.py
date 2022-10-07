from django.contrib import admin
from django.urls import path,include
from pages import views


urlpatterns = [
    path('',views.home,name="home" ),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),
    path('contact',views.ContactView.as_view(),name="contact")
]
