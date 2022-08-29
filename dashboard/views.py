
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from movieshd.forms import *
from .forms import *

from movieshd.models import *
from.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here
def admin_reg(request):
    if request.method == 'POST':
        username = request.POST.get('admin_username', '')
        email = request.POST.get('admin_email', '')
        password = request.POST.get('admin_password', '')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('/dash')
    else:

        return render(request, 'user/admin_reg.html')


def adminlogin(request):
    if request.method  == 'POST':
        username = request.POST.get('adminusername')
        password = request.POST.get('adminpassword')
        User=authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
        return redirect('/dash')
    return render(request,'user/adminlogin.html')

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='adminlogin')
def dash(request):
    if request.user.is_superuser:
        total_user=User.objects.all()
        total_movies=add_categories.objects.all()
        list = add_categories.objects.all()
        list_paginator = Paginator(list, 8)
        page_number = request.GET.get('page')
        page = list_paginator.get_page(page_number)
        context ={
            'count':total_movies.count,
            'count1':total_user.count,
            'count': list_paginator.count,
            'page': page,
        }
        return render(request, 'dashboard/index.html',context)
    else:
        return redirect('/')

@login_required(login_url='adminlogin')
def movies_list(request):
    list = add_categories.objects.all()
    list_paginator = Paginator(list, 8)
    page_number = request.GET.get('page')
    page = list_paginator.get_page(page_number)
    context = {
        'count': list_paginator.count,
        'page': page,

    }
    return render(request, 'dashboard/movies_list.html',context)

@login_required(login_url='adminlogin')
def users(request):
    um = Subscription.objects.all()
    return render(request,'dashboard/users.html',{'user':um})

@login_required(login_url='adminlogin')
def comment(request):
    return render(request,'dashboard/comments.html')

@login_required(login_url='adminlogin')
def payments(request):
    um = Subscription.objects.all()
    return  render(request,'dashboard/reviews.html', {'um':um})

def logout_user(request):
    logout(request)
    return redirect('/')

# demoadd views
@login_required(login_url='adminlogin')
def update_status(request,status,id):
    add_categories.objects.filter(id=id).update(status=status)
    return redirect('/list')

# def update(request):
#     if request.method == "POST":
#         pb_form = publisher_form(request.POST, request.FILES)
#         if pb_form.is_valid():
#             pb_form.save()
#             return redirect('/update')
#     else:
#         pb_form =publisher_form()
#     return render(request, 'dashboard/update.html',{'pb_form': pb_form})


@login_required(login_url='adminlogin')
def pub_update_movie(request, id):
    pb = add_categories.objects.get(pk=id)
    pmu = publisher_form(instance=pb)
    ab = publisher_form(request.POST,request.FILES,instance=pb)
    if ab.is_valid():
        ab.save()
        ab.save()
        return redirect('/list')
    return render(request, 'dashboard/update.html', {'pb_form':pmu})

@login_required(login_url='adminlogin')
def pub_delete_movie(request, id):
    dl = add_categories.objects.get(pk=id)
    dl.delete()
    return redirect('/list')

def search(request):
    if request.method == "GET":
        search = request.GET.get('search')
        post = add_categories.objects.all().filter(title=search)
        am = add_categories.objects.all()
        return render(request, 'searchbar.html', {'post': post, 'am': am})


# action="/searchbar"

@login_required(login_url='/adminlogin')
def update_user(request, id):
    upuser = User.objects.get(pk=id)
    a=userform(instance=upuser)
    if request.method == "POST":
        user = userform(request.POST, instance=upuser)
        user.save()
        return redirect('/user')
    return render(request, 'dashboard/userupdate.html', {'form':a})

@login_required(login_url='/adminlogin')
def delete_user(request, id):
    deluser = User.objects.get(pk=id)
    deluser.delete()
    return redirect('/user')


def test1(request):
    user=User.objects.all()
    mem=UserMembership.objects.all()
    return render(request, 'test.html', {'user':user, 'mem':mem})

def addmovie(request):
    if request.method == "POST":
        pb_form = publisher_form(request.POST, request.FILES)
        if pb_form.is_valid():
            pb_form.save()
            return redirect('/list')
    else:
        pb_form =publisher_form()
    return render(request, 'dashboard/add_movies.html', {'pb_form': pb_form})
