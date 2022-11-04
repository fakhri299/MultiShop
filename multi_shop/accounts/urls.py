from django.urls import path
from accounts import views

urlpatterns = [
    path('contact',views.contact,name='contact'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('register',views.register_user,name='register'),
    
  
]
