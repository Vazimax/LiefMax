from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Order, Review
from .forms import OrderForm, ReviewForm, UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages


@login_required
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        if phone_number:
            profile.phone_number = phone_number
            profile.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
        else:
            messages.error(request, 'Phone number is required.')
            
    return render(request, 'accounts/profile.html', {'profile': profile})


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
def claim_order_page(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.is_claimed:
        return JsonResponse({'error': 'Order already claimed'}, status=400)

    if request.method == 'POST':
        expected_delivery_time = request.POST.get('expected_delivery_time')

        if expected_delivery_time:
            order.is_claimed = True
            order.delivery_agent = request.user
            order.save()

            request.user.profile.expected_delivery_time = expected_delivery_time
            request.user.profile.save()

            return redirect('deliveries')
        else:
            return JsonResponse({'error': 'Phone number and delivery time required'}, status=400)

    return render(request, 'orders/claim_order_page.html', {'order': order})

@login_required
def deliveries(request):
    claimed_orders = Order.objects.filter(delivery_agent=request.user)
    return render(request, 'orders/deliveries.html', {'claimed_orders': claimed_orders})

@login_required
def client_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/client_orders.html', {'orders': orders})


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
    return redirect('order_list')

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user instance
            phone_number = form.cleaned_data['phone_number']
            # Create a profile and assign the phone number
            user.profile.phone_number = phone_number
            user.profile.save()
            login(request, user)
            return redirect('order_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

from django.shortcuts import redirect

@login_required
def confirm_delivery(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if not order.is_confirmed:
        order.is_confirmed = True
        order.save()
    return redirect('client_order')

@login_required
def confirm_delivery_agent(request, order_id):
    order = get_object_or_404(Order, id=order_id, delivery_agent=request.user)
    if not order.is_delivery_agent_confirmed:
        order.is_delivery_agent_confirmed = True
        order.save()
    return redirect('deliveries')

@login_required
def confirm_cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Ensure only the user who ordered or the delivery agent can access this
    if order.user != request.user and order.delivery_agent != request.user:
        return redirect('order_list')  # Redirect if unauthorized

    return render(request, 'orders/confirm_cancel.html', {'order': order})

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Ensure only the user who ordered or the delivery agent can cancel
    if order.user != request.user and order.delivery_agent != request.user:
        return redirect('order_list')  # Redirect if unauthorized

    if order.delivery_agent == request.user:
        order.delivery_agent = None  # Unassign delivery agent
        order.is_canceled = True  # Mark as canceled
        order.cancellation_reason = "Delivery agent canceled"
    else:
        order.is_canceled = True
        order.cancellation_reason = "Orderer canceled"

    order.is_claimed = False
    order.save()
    return redirect('order_list')  # Redirect after cancellation