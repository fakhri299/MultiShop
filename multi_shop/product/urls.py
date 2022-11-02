from django.urls import path
from product import views


urlpatterns = [
   path('store',views.shop,name='store'),
   path('product/<int:id>',views.detail,name='product_detail')
   
]
