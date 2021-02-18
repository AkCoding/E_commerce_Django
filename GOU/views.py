from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Contact
from math import ceil
from django.contrib.auth import authenticate, login, logout
import pyautogui
from PIL import Image, ImageGrab
import time


def home(request):
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])
    params = {'allprods': allprods}
    return render(request, 'gou/home.html', params)


def SearchMatch(query, item):
    if query in item.product_name.lower() or query in item.product_desc.lower() or query in item.category.lower() or query in item.subcategory.lower() or query in str(item.price):
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if SearchMatch(query, item)]
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nslides), nslides])
    params = {'allprods': allprods,"msg":""}
    if len(allprods)==0 or len(query)<3 :
        params={'msg':"Product Not Found"}
    return render(request, 'gou/search.html', params)


def about(request):
    context = {'data': Product.objects.all()}
    return render(request, 'gou/about.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'gou/contact.html')


def track(request):
    return render(request, 'gou/track.html')


def productview(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'gou/productview.html', {'products': product[0]})


def checkout(request):
    return render(request, 'gou/checkout.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if len(username) < 10:
            messages.error(request, 'username must be 10 character')
            return redirect('GouHome')
        if not username.isalnum():
            messages.error(request, 'username contain only alpha and  numeric')
            return redirect('GouHome')
        if len(email) < 10:
            messages.error(request, 'Your email address is wrong')
            return redirect('GouHome')
        if not len(phone) == 10 or phone == int():
            messages.error(request, 'Your phone no is wrong')
            return redirect('GouHome')
        if len(password1) < 8:
            messages.error(request, 'Your password is too short')
            return redirect('GouHome')
        if len(password1) > 12:
            messages.success(request, 'Your password is too long')
            return redirect('GouHome')
        if password1 != password2:
            messages.error(request, 'Your password are not match')
            return redirect('GouHome')

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone = phone
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('GouHome')
    else:
        return HttpResponse('404 - Not Found')

    return render(request, 'gou/signup.html')


def userlogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in..")
            return redirect('GouHome')
        else:
            messages.error(request, "Invalid Username & Password")
            return redirect('GouHome')
    return HttpResponse('404 - Not Found')


def userlogout(request):
    pyautogui.press('ese')
    image = ImageGrab.grab()
    image.show()
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('GouHome')

