from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrderForm(forms.ModelForm):
    preferred_delivery_time = forms.TimeField(widget=forms.Select(choices=[
        ("07:00", "7:00 AM"),
        ("07:15", "7:15 AM"),
        ("07:30", "7:30 AM"),
        ("07:45", "7:45 AM"),
        ("08:00", "8:00 AM"),
        ("08:15", "8:15 AM"),
        ("08:30", "8:30 AM"),
        ("08:45", "8:45 AM"),
        ("09:00", "9:00 AM"),
        ("09:15", "9:15 AM"),
        ("09:30", "9:30 AM"),
        ("09:45", "9:45 AM"),
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
        ("22:00", "10:00 PM"),
        ("23:00", "11:00 PM"),
        ("00:00", "12:00 AM"),
        ("01:00", "1:00 AM"),

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
