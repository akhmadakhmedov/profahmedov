from django.shortcuts import render
from . models import Contact
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "mysite/index.html")

def contact(request):
    if request.method == "POST":
        name_r = request.POST.get('Name_Surname')
        phone_r = request.POST.get('Phone_number')
        subject_r = request.POST.get('Subject')
        message_r = request.POST.get('Message')
        d = Contact(Name_Surname = name_r, Phone_number=phone_r, Subject=subject_r,Message=message_r)
        d.save()
        messages.success(request, "Спасибо. Ваше сообщение принято!")
        return render(request, 'mysite/contact.html')
        
    
    else:
        return render(request, "mysite/contact.html")

def portfolio(request):
    return render(request, "mysite/portfolio.html")

def pricing(reques):
    return render(reques, 'mysite/pricing.html')

