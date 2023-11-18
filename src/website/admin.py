from django.contrib import admin
from . import models
admin.register(models.Product)
admin.register(models.Customer)
admin.register(models.Order)
admin.register(models.OrderItems)
admin.register(models.ShippingAddress)
# Register your models here.
