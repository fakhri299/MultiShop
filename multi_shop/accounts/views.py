from django.shortcuts import render,redirect
from accounts.forms import ContactForm,RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout





def register_user(request):
    if request.method == 'POST':
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form=RegisterForm()

    return render(request,'register.html',{'form':form})



def login_user(request):
    if request.method == 'POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')

            else:
                messages.info(request,'User is not exist')


    else:
        form=LoginForm()

    return render(request,'login.html',{'form':form})


def logout_user(request):
    logout(request)
    return redirect('login')



			
def contact(request):
    if request.method == 'POST':
        form=ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'We got your message,  we connect with you soon')

    else:
        form=ContactForm()

    return render(request,'contact.html',{'form':form})





    # if request.method == "GET":
    #     form = ContactForm()
    # else:
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         subject = form.cleaned_data["subject"]
    #         from_email = form.cleaned_data["from_email"]
    #         message = form.cleaned_data['message']
    #         try:
    #             send_mail(subject, message, from_email, ["admin@example.com"])
    #         except BadHeaderError:
    #             return HttpResponse("Invalid header found.")
    #         return redirect("success")
    # return render(request, "email.html", {"form": form})


# class ContactView(SuccessMessageMixin,FormView):
#     template_name='contact.html'
#     form_class= ContactForm
#     success_url=reverse_lazy('contact')
#     success_message='We recieved your request'
    
#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)

