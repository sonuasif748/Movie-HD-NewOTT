import requests
from django.shortcuts import render

# Create your views here.
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import razorpay


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("loginusername")
        password = request.POST.get("loginpassword")
        User = authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect("/")
    return render(request, 'login.html')


def register_page(request):
    userform = CustomerUserForm()
    customerform = CustomerForm()
    mydict = {'userform': userform, 'customerform': customerform}
    if request.method == "POST":
        userform = CustomerUserForm(request.POST)
        customerform = CustomerForm(request.POST, request.FILES)
        if userform.is_valid() and customerform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
            customer = customerform.save(commit=False)
            customer.user = user
            customer.save()
            user.groups.add(Group.objects.get(name='customer'))
            return redirect('/')
    return render(request, 'base.html', context=mydict)


def logoutuser(request):
    logout(request)
    return redirect('/')


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("adminusername")
        password = request.POST.get("adminpassword")
        User = authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect("/dash")
    return render(request, 'login.html')


def telugumovie(request):
    tm = add_categories.objects.filter(language='Telugu')
    return render(request, 'telugu.html', {'tm': tm})


def tamilmovie(request):
    tam = add_categories.objects.filter(language='Tamil')
    return render(request, 'tamil.html', {'tam': tam})


def malayalammovie(request):
    mm = add_categories.objects.filter(language='Malayalam')
    return render(request, 'malayalam.html', {'mm': mm})


def hindimovie(request):
    hm = add_categories.objects.filter(language='Hindi')
    return render(request, 'hindi.html', {'hm': hm})


def englishmovie(request):
    em = add_categories.objects.filter(language='English')
    return render(request, 'english.html', {'em': em})


def actionmovie(request):
    action_movies = add_categories.objects.filter(geners='Action')
    return render(request, 'action.html', {'action_movie': action_movies})


def dramamovie(request):
    drama_movies = add_categories.objects.filter(geners='Drama')
    return render(request, 'drama.html', {'drama_movie': drama_movies})


def thrillermovie(request):
    thriller_movie = add_categories.objects.filter(geners='Thirller')
    return render(request, 'thriller.html', {'thriller_movie': thriller_movie})


def movies(request):
    am = add_categories.objects.all()
    return render(request, 'genres.html', {'am': am})


def homepage(request):
    mv = add_categories.objects.all().filter(status=1)
    tm = mv.filter(language='Telugu')
    hm = mv.filter(language='Hindi')
    em = mv.filter(language='English')
    mm = mv.filter(language='Malayalam')
    tam = mv.filter(language='Tamil')
    return render(request, 'home.html', {'mv': mv, 'tm': tm, 'hm': hm, 'em': em, 'mm': mm, 'tam': tam})


@login_required(login_url='login_page')
def moviedetail(request, id):
    user_membership = UserMembership.objects.get(user=request.user)
    subscriptions = Subscription.objects.filter(user_membership=user_membership).exists()
    if subscriptions == False:
        return redirect('subscription')
    else:
        detail = add_categories.objects.get(pk=id)
        mv = add_categories.objects.all()
        return render(request, 'moviedescri.html', {'detail': detail, 'mv': mv})


def banner(request):
    movieshow = add_categories.objects.all().filter(status=1)
    return render(request, 'banner.html', {'movie': movieshow})


@login_required(login_url='login_page')
def subscription(request):
    return render(request, 'subscription.html')

@login_required(login_url='login_page')
def paymentgate(request):
    plan = request.GET.get('sub_plan')
    fetch_membership = Membership.objects.filter(membership_type=plan).exists()
    if fetch_membership == False:
        return redirect('paymentgate')
    else:
        membership = Membership.objects.get(membership_type=plan)
        price = float(membership.price) * 100
        price = int(price)
        client = razorpay.Client(auth=("rzp_test_57W21Kxo1htc3H", "2RTv8Kd5PWkXKBW9lKwsNWlf"))
        order_currency = 'INR'
        payment_order = client.order.create(dict(amount=price, currency=order_currency, payment_capture=1))
        payment_order_id = payment_order['id']
        context = {
            'order_amount': price,
            'order_amount2': price / 100,
            'order_id': payment_order_id,
            'membership': membership
        }
        data = UserMembership(user=request.user, membership=membership, amount=price, order_id=payment_order_id)
        data.save()
    return render(request, 'paymentgate.html', context)
