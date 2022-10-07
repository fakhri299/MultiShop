from django.urls import path
from accounts import views

urlpatterns = [
    path('signup',views.sign_up,name='signup'),
    path('signin',views.sign_in,name='signin'),
]
