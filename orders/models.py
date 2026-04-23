from django.db import models
from customers.models import customer
from products.models import products

# Create your models here.
class Order(models.Model):
    LIVE = 1
    DELETE = 0
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSESD = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES = ((ORDER_PROCESSESD,'OrderProcessesd'),
                      (ORDER_DELIVERED,'OrderDelivered'),
                      (ORDER_REJECTED,'OrderRejected'))
    delete_choices = ((LIVE,'Live'),(DELETE,'Delete'))
    owner = models.ForeignKey(customer,on_delete=models.SET_NULL,related_name="orders",null=True)
    delete_status = models.IntegerField(choices = delete_choices,default = LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Odered_item(models.Model):
    product = models.ForeignKey(products,related_name="ordered_items",on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="added_items")