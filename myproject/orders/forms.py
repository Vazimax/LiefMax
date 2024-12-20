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
        ("10:15", "10:15 AM"),
        ("10:30", "10:30 AM"),
        ("10:45", "10:45 AM"),
        ("11:00", "11:00 AM"),
        ("11:15", "11:15 AM"),
        ("11:30", "11:30 AM"),
        ("11:45", "11:45 AM"),
        ("12:00", "12:00 PM"),
        ("12:15", "12:15 PM"),
        ("12:30", "12:30 PM"),
        ("12:45", "12:45 PM"),
        ("13:00", "1:00 PM"),
        ("13:15", "1:15 PM"),
        ("13:30", "1:30 PM"),
        ("13:45", "1:45 PM"),
        ("14:00", "2:00 PM"),
        ("14:15", "2:15 PM"),
        ("14:30", "2:30 PM"),
        ("14:45", "2:45 PM"),
        ("15:00", "3:00 PM"),
        ("15:15", "3:15 PM"),
        ("15:30", "3:30 PM"),
        ("15:45", "3:45 PM"),
        ("16:00", "4:00 PM"),
        ("16:15", "4:15 PM"),
        ("16:30", "4:30 PM"),
        ("16:45", "4:45 PM"),
        ("17:00", "5:00 PM"),
        ("17:15", "5:15 PM"),
        ("17:30", "5:30 PM"),
        ("17:45", "5:45 PM"),
        ("18:00", "6:00 PM"),
        ("18:15", "6:15 PM"),
        ("18:30", "6:30 PM"),
        ("18:45", "6:45 PM"),
        ("19:00", "7:00 PM"),
        ("19:15", "7:15 PM"),
        ("19:30", "7:30 PM"),
        ("19:45", "7:45 PM"),
        ("20:00", "8:00 PM"),
        ("20:15", "8:15 PM"),
        ("20:30", "8:30 PM"),
        ("20:45", "8:45 PM"),
        ("21:00", "9:00 PM"),
        ("21:15", "9:15 PM"),
        ("21:30", "9:30 PM"),
        ("21:45", "9:45 PM"),
        ("22:00", "10:00 PM"),
        ("22:15", "10:15 PM"),
        ("22:30", "10:30 PM"),
        ("22:45", "10:45 PM"),
        ("23:00", "11:00 PM"),
        ("23:15", "11:15 PM"),
        ("23:30", "11:30 PM"),
        ("23:45", "11:45 PM"),
        ("00:00", "12:00 AM"),
        ("00:15", "12:15 AM"),
        ("00:30", "12:30 AM"),
        ("00:45", "12:45 AM"),
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
