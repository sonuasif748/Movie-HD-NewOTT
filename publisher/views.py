from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,Group
from django.http import HttpResponse
from movieshd.forms import *

from movieshd.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from movieshd.forms import *

# Create your views here.
@login_required(login_url='pub_login')
def publisher_add(request):
    if request.method == "POST":
        pb_form = publisher_form(request.POST, request.FILES)
        if pb_form.is_valid():
            pb_form.save()
            return redirect('/publisher')
    else:
        pb_form =publisher_form()
    return render(request, 'publisher1/pub_add.html', {'pb_form': pb_form})

@login_required(login_url='pub_login')
def publish(request):
    u=User.objects.all()
    list = add_categories.objects.all()
    list_paginator=Paginator(list,8)
    page_number=request.GET.get('page')
    page=list_paginator.get_page(page_number)
    context={
        'count':list_paginator.count,
        'page':page,
        'count1':u.count
    }
    return  render(request,'publisher1/index.html',context)

@login_required(login_url='pub_login')
def publist(request):
    u = User.objects.all()
    list = add_categories.objects.all()
    list_paginator = Paginator(list, 8)
    page_number = request.GET.get('page')
    page = list_paginator.get_page(page_number)
    context = {
        'count': list_paginator.count,
        'page': page,
        'count1': u.count
    }
    return  render(request,'publisher1/pub_list.html', context)

def is_publisher(user):
    return user.groups.filter(name='publisher').exists()

def pub_login(request):
    if request.method  == 'POST':
        username = request.POST.get('pubusername')
        password = request.POST.get('pubpassword')
        User=authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
            if is_publisher(request.user):
                return redirect('/publisher')
            else:
                return redirect('pub_login')
    return render(request,'publisher1/publisherlogin.html')

def pub_reg(request):
    userform = CustomerUserForm()
    publisherform = PublisherForm()
    mydict = {'userform': userform, 'publisherform': publisherform}
    if request.method == "POST":
        userform = CustomerUserForm(request.POST)
        publisherform = PublisherForm(request.POST, request.FILES)
        if userform.is_valid() and publisherform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            publisher = publisherform.save(commit=False)
            publisher.user = user
            publisher.save()
            user.groups.add(Group.objects.get(name='publisher'))
            return redirect('/pub_login')
    return render(request, 'publisher1/pub_reg.html', context=mydict)