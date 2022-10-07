from django.urls import path
from product import views


urlpatterns = [
   path('',views.all_products,name='all_products'),
   path('<int:product_id>',views.detail_product,name='detail_products'),
   
]
