from django.urls import path
from . import views


urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('', views.order_list, name='order_list'),
    path('claim_order/<int:order_id>/', views.claim_order_page, name='claim_order_page'),
    path('rate_user/<int:user_id>/', views.rate_user, name='rate_user'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('deliveries/', views.deliveries, name='deliveries'),
    path('client_orders/', views.client_orders, name='client_orders'),
    path('profile/', views.profile_view, name='profile'),
    path('confirm_delivery/<int:order_id>/', views.confirm_delivery, name='confirm_delivery'),
    path('confirm_delivery_agent/<int:order_id>/', views.confirm_delivery_agent, name='confirm_delivery_agent'),
    path('order/<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    path('order/<int:order_id>/confirm_cancel/', views.confirm_cancel_order, name='confirm_cancel_order'),
    path('orders/<int:order_id>/cancel/', views.confirm_cancel_order, name='confirm_cancel_order'),

]