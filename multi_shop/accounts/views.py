from django.shortcuts import render,redirect
from accounts.forms import ContactForm
from django.views.generic.edit import FormView
from django.contrib import messages


# class ContactView(SuccessMessageMixin,FormView):
#     template_name='contact.html'
#     form_class= ContactForm
#     success_url=reverse_lazy('contact')
#     success_message='We recieved your request'
    
#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)


def contact(request):
    if request.method == 'POST':
        form=ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Mesajınızı aldıq tezliklə sizinlə əlaqə saxlanılacaq')

            

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
