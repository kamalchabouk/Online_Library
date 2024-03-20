from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django import forms
from django.shortcuts import redirect, render

from django.contrib.auth.models import AbstractUser
from django.db import models



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ["username", "email", "password1", "password2"]


def  registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("index")
    else:
        form = RegistrationForm()

#-- new Code - Custom User

# class CustomUser(AbstractUser):
#     userid = models.CharField(max_length=50, unique=True)
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     address = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     age = models.PositiveIntegerField()
#     order_history = models.ManyToManyField('Order', blank=True)

# class Order(models.Model):
#     # Add any additional fields you want here, for example:
#     # date = models.DateTimeField(auto_now_add=True)
#     pass


    return render(request, "registration/register.html", {"form" : form})


def index(request):
    return render(request,"index.html")
        