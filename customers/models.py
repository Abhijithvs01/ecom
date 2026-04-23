from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class customer(models.Model):
    LIVE = 1
    DELETE = 0
    delete_choices = ((LIVE,'Live'),(DELETE,'Delete'))
    name = models.CharField(max_length=200)
    address = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="Customer_Profile")
    phone  = models.CharField(max_length=10)
    priority = models.IntegerField(default=0)
    delete_status = models.IntegerField(choices = delete_choices,default = LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self)-> str: 
        return self.name