from django.contrib import admin
from orders.models import Order_item,Order

admin.site.register(Order)
admin.site.register(Order_item)

# Register your models here.
