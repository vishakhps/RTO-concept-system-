from django.contrib.messages.api import warning
from django.shortcuts import render,redirect
from rtoapp.models import UserDetails
from adminapp.forms import UserDetailsForm
from django.contrib import messages
# Create your views here.


def home(request):
    user = request.user.userdetails
    form = UserDetailsForm(instance=user)
    if user.get_insurance_status == 'Expired'and user.get_registration_status == 'Expired' and user.get_Pollution_status == 'Expired':
        {
             messages.warning(request, "Your Insurance ,Your Vehicle registration certificate and Your pollution certificate is expire")
             
        }
    elif user.get_insurance_status == 'Expired'and user.get_registration_status == 'Expired':
        {
             messages.warning(request, "Your Insurance and Your Vehicle registration certificate is expired")
        }
    elif user.get_insurance_status == 'Expired'and user.get_Pollution_status == 'Expired':
        {
             messages.warning(request, "Your Insurance and Your pollution certificate is expired")
        }  
    elif user.get_registration_status == 'Expired'and user.get_Pollution_status == 'Expired':
        {
             messages.warning(request, "Your Vehicle registration certificate and Your pollution certificate is expired")
        }    
    elif user.get_Pollution_status == 'Expired':
        messages.warning(request,"Your Pollution Certificate has Expired")
    elif user.get_insurance_status == 'Expired':
        messages.warning(request, "Your Insurance is expired")

    elif user.get_registration_status == 'Expired':
        messages.warning(request, "Your Registration is expired")
   
    context = {
        'user':user,
        'form':form,
    }
    return render(request,'userapp/index.html',context)
def wallet(request):
    return render(request, 'userapp/wallet.html')


def user_insurance(request):
    
    return render(request,'userapp/form.html')

