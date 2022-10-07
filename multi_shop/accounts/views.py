import re
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from accounts.forms import SigninForm,SignupForm


# Create your views here.

#SIGN_UP
def sign_up(request):
    
    if request.method == 'POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request,"You signed up successfully")
            return redirect('signin')
    
    else:
        form=SignupForm()


    return render(request,'signup.html',{'form':form})


#SIGN_IN

def sign_in(request):
    if request.method =='POST':
        form=SigninForm(request.POST)

        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(request,email=email,password=password)

            if user is not None:
                if user.is_active():
                    login(request,user)
                    return redirect('home')

                else:
                    messages.info(request,"Disabled account")
            
            else:
                messages.info(request,"User wasn't found,check your email or password")


    else:
        form=SigninForm()
        

    return render (request,'signin.html',{'form':form})




