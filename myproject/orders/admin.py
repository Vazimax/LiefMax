from django.contrib import admin
from .models import *


admin.site.register(Order)
admin.site.register(Profile)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery_agent', 'is_claimed', 'is_confirmed', 'is_delivery_agent_confirmed')
