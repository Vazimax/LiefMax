from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    preferred_delivery_time = forms.TimeField(widget=forms.Select(choices=[
        ("06:00", "6:00 AM"),
        ("07:00", "7:00 AM"),
        ("08:00", "8:00 AM"),
        ("09:00", "9:00 AM"),
        ("10:00", "10:00 AM"),
        ("11:00", "11:00 AM"),
        ("12:00", "12:00 PM"),
        ("13:00", "1:00 PM"),
        ("14:00", "2:00 PM"),
        ("15:00", "3:00 PM"),
        ("16:00", "4:00 PM"),
        ("17:00", "5:00 PM"),
        ("18:00", "6:00 PM"),
        ("19:00", "7:00 PM"),
        ("20:00", "8:00 PM"),
        ("21:00", "9:00 PM"),
    ]))

    class Meta:
        model = Order
        fields = ['location', 'items', 'preferred_delivery_time', 'category']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Enter your phone number.')

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
