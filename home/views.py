from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from . models  import Enquiry

# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        enquiry = Enquiry(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        enquiry.save()
        messages.success(request, 'Your message sent successfully')
    return render(request, 'index.html')

def enquiry(request):
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     desc = request.POST.get('desc')
    #     enquiry = Enquiry.objects.create(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
    #     enquiry.save()
        # messages.success('Your message sent successfully')
    return render(request, 'index.html')