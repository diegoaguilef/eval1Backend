from django.db import models

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
