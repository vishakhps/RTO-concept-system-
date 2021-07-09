from django.shortcuts import redirect, render
from .forms import CreateUserForm , UserDetailsForm,number_plate_forms
from django.contrib import messages
from rtoapp.models import UserDetails,user_nuberplate_details,number_plate
from datetime import date
from django.contrib.auth.models import Group
import imutils
import pytesseract
import datetime
import cv2
import os
import numpy as np
# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def home(request):
    return render(request,'adminapp/index.html')


def user_list(request):
    users = UserDetails.objects.all()
    context = {
        'users':users,
    }
    return render(request,'adminapp/user_list.html', context)



def user_update(request,n):
    user = UserDetails.objects.get(id = n)
    form = UserDetailsForm(instance=user)
    if request.method == "POST":
        form =  UserDetailsForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"user updated successfully")
            return redirect('admin-user-list')
    context = {
        'user':user,
        'form':form,
    }
    return render(request,'adminapp/update_form.html', context)


def user_registration(request):
    form = CreateUserForm()
    form2 = UserDetailsForm()
    user = None
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
        else:
            messages.warning(request,"please check the user details entered")
        if user is not None:
            details ,created = UserDetails.objects.get_or_create(user = user,email = user.email)
            form2 = UserDetailsForm(request.POST, instance = details)
            if form2.is_valid():
                obj = form2.save()
                group =  Group.objects.get(name='user')
                user.groups.add(group)
                return redirect('admin-user-list')
    context = {
        'form':form,
        'form2':form2,
    }

    return render(request,'adminapp/update_form.html',context)


def number_plate_detection(request):
    global a 
    form = number_plate_forms()
    if request.method == 'POST':
        print(os.getcwd())
        form = number_plate_forms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            text_no =None
            var =number_plate.objects.all().last()
            print(var)
            path=var.Number_plate.url
            print(path)
            print(os.getcwd())
            img = cv2.imread(os.getcwd()+path)
            img = imutils.resize(img, width=500)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_img = cv2.bilateralFilter(gray_img, 11, 17, 17)
            try:
                c_edge = cv2.Canny(gray_img, 170, 200)
                cnt, new = cv2.findContours(c_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
                cnt = sorted(cnt, key=cv2.contourArea, reverse=True)[:30]
                NumberPlateCount = None
                im2 = img.copy()
                cv2.drawContours(im2, cnt, -1, (0, 255, 0), 3)
                count = 0
                for c in cnt:
                    perimeter = cv2.arcLength(c, True)  # Getting perimeter of each contour
                    approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
                    if len(approx) == 4:  # Selecting the contour with 4 corners/sides.
                        NumberPlateCount = approx
                        break
                masked = np.zeros(gray_img.shape, np.uint8)
                new_image = cv2.drawContours(masked, [NumberPlateCount], 0, 255, -1)
                new_image = cv2.bitwise_and(img, img, mask=masked)
                text_no1 = pytesseract.image_to_string(new_image,
                                                       config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
                print(text_no1)
                text_no = pytesseract.image_to_string(new_image, config='--psm 7')
                print(text_no)
                if len(text_no1) > len(text_no):
                    text_no = text_no1
                    special_list = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '\x0c', '+',
                                    '=',
                                    '{', '}', '[', ']', '|', '\'', "/", ":", ";", '"', "'", '<', '>', ',', ".", '?',
                                    '\n',
                                    '\t', '\r', '°', ' ', '  ', '   ', '', '    ']
                    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                               's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                list1 = []
                for i in text_no:
                    if i not in special_list and i in letters:
                        print(i)
                        list1.append(i)
                if len(list1) == 0:
                    text_no = None
                print('list is', list1)
                print(text_no)

            except:
                print("Not possible")
            finally:
                if text_no is None:
                    form = number_plate_forms()
                    return render(request, 'adminapp/update_form.html',
                                      {'msg': 'OCR is not applicable for this image', 'form': form, 'name': 'image'})

                else:
                    v = user_nuberplate_details(date=datetime.datetime.now(), license_number=text_no[0:15])
                    v.save()
                    print(text_no)
                    a = text_no
                    form = number_plate_forms()
                    context = {
                        'form': form,
                    }
                    return render(request, 'adminapp/update_form.html',
                                  {'msg': text_no,'form': form})

    else:
        form = number_plate_forms()
        context = {
            'form': form
        }
    return render(request, 'adminapp/update_form.html', context)

def check(request):
    user = UserDetails.objects.get(id = 7)
    form = UserDetailsForm(instance=user)
    if request.method == "POST":
        form =  UserDetailsForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"user updated successfully")
            return redirect('admin-user-list')
    context = {
        'user':user,
        'form':form,
    }
    return render(request,'adminapp/update_form.html', context)

def check2(request):
    user = UserDetails.objects.get(id = 5)
    form = UserDetailsForm(instance=user)
    if request.method == "POST":
        form =  UserDetailsForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,"user updated successfully")
            return redirect('admin-user-list')
    context = {
        'user':user,
        'form':form,
    }
    return render(request,'adminapp/update_form.html', context)



