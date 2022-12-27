from django.db import models
from django.db.models import Sum
from users.models import User
from django.db import transaction
from django.core.exceptions import ValidationError
import random

# Create your models here.
class Printer(models.Model):
    BRANDS = [['hp', 'HP'], ['brother', 'Brother'],['cannon', 'Cannon'], ['lg', 'LG'], ['samsung', 'Samsung']]
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    serial_number = models.TextField()
    brand = models.CharField(max_length=20, choices=BRANDS)
    is_wifi = models.BooleanField(default=False)
    price = models.IntegerField()
    stock = models.IntegerField()
    created_at = models.DateTimeField()
    image = models.ImageField(default=None, null=True, upload_to='printer_images')

    def __str__(self):
        return 'Impresora: %s, Description: %s, Serial: %s, Brand: %s, is_wifi: %s, Price: %s, Stock: %s, Created: %s'%(
            self.name, self.description, self.serial_number, self.brand, self.is_wifi, self.price, self.stock, self.created_at)

class ShoppingCart(models.Model):

    @staticmethod
    def product_quantities(user_id, printer_id):
        return ShoppingCart.objects.filter(
            user_id=user_id, printer_id=printer_id
        ).aggregate(quantities=Sum('quantity'))

    id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField()
    enabled = models.BooleanField(default=True)
    printer = models.ForeignKey(
        Printer,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )   

    def total_price(self):
        return self.quantity * self.printer.price

    
class Sale(models.Model):
    id = models.IntegerField(primary_key=True)
    invoice = models.TextField(unique=True)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='sold_items',
    )
    shopping_carts = models.ManyToManyField(ShoppingCart)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
