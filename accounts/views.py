from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from categories.models import Category
from productType.models import ProductType
import re


def all_categories():
    return Category.objects.all()


def all_productTypes():
    return ProductType.objects.all()


def index(request):
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, 'index.html', {"categories": categories,
                                          "productTypes": productTypes})


def login_input_fields(request, login_form):
    """Log in as user by filling in registered username and password"""
    username = login_form['username'].value()
    password = login_form['password'].value()

    if username is None or username == "":
        messages.error(request, 'your username is required')
        return False
    if password is None or password == "":
        messages.error(request, 'password is required')
        return False

    return True


@login_required
def logout(request):
    """"Check to see if the user is logged in before
        executing any more of the code"""
    auth.logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    categories = all_categories()
    productTypes = all_productTypes()
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_input_fields(request, login_form) is False:
            args = {'login_form': login_form,
                    'next': request.GET.get('next', '')}
            return render(request, 'login.html', args,
                          {"categories": categories,
                           "productTypes": productTypes})

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.success(request, "Succesfully logged in")

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))

            else:
                login_form.add_error("username",
                                     "Combination of username and password is incorrect")
    else:
        login_form = UserLoginForm()

    args = {
        'login_form': login_form,
        'next': request.GET.get('next', ''),
        'categories': categories,
        'productTypes': productTypes
        }
    return render(request, 'login.html', args)


def registration_input_fields(request, registration_form):
    """Registration form to registrate new user"""
    email = registration_form['email'].value()
    username = registration_form['username'].value()
    password1 = registration_form['password1'].value()
    password2 = registration_form['password2'].value()

    if email is None or email == "":
        messages.error(request, 'an email address is required')
        return False
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        messages.error(request, 'a valid email address is required')
        return False
    if username is None or username == "":
        messages.error(request, 'your username is required')
        return False
    if password1 is None or password1 == "":
        messages.error(request, 'password is required')
        return False
    if password2 is None or password2 == "":
        messages.error(request, 'confirmation password is required')
        return False

    if password1 != password2:
        messages.error(request, 'passwords do not match')
        return False

    return True


def registration(request):
    """Render registration page"""
    # if request.user.is_authenticated:
    #     return redirect(reverse('index'))
    categories = all_categories()
    productTypes = all_productTypes()
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_input_fields(request, registration_form) is False:
            args = {'registration_form': registration_form}
            return render(request, 'registration.html', args,
                          {"categories": categories,
                           "productTypes": productTypes})

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     email=request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "Succesfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register this account")

    else:
        registration_form = UserRegistrationForm()

    args = {
        'registration_form': registration_form,
        'categories': categories,
        'productTypes': productTypes
        }
    return render(request, 'registration.html', args)


def user_profile(request):
    """User profile page"""
    user = User.objects.filter(email=request.user.email)
    categories = all_categories()
    productTypes = all_productTypes()
    return render(request, 'profile.html',
                  {"profile": user, "categories": categories,
                   "productTypes": productTypes})
