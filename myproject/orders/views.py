from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Order, Review
from .forms import OrderForm, ReviewForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


@login_required
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/place_order.html', {'form': form})


def order_list(request):
    orders = Order.objects.filter(is_claimed=False).order_by('preferred_delivery_time')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def claim_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if not order.is_claimed:
        order.delivery_agent = request.user
        order.is_claimed = True
        order.save()
        order.delete()
        return redirect('order_list')
    return JsonResponse({'error': 'Order already claimed'}, status=400)

@login_required
def rate_user(request, user_id):
    reviewee = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.reviewee = reviewee
            review.save()
            return redirect('profile', user_id=user_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/rate_user.html', {'form': form, 'reviewee': reviewee})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('order_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('order_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
