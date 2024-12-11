from django.urls import path
from . import views


urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('order_list/', views.order_list, name='order_list'),
    path('claim_order/<int:order_id>/', views.claim_order, name='claim_order'),
    path('rate_user/<int:user_id>/', views.rate_user, name='rate_user'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]