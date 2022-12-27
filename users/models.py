from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    role = models.CharField(max_length=25, default="user")
    image = models.ImageField(default=None, null=True, upload_to='users_images')
    phone = models.CharField(max_length=12, default="+56999999999", null=True)
    address = models.CharField(max_length=100, default="", null=True)
    region = models.CharField(max_length=100, default="", null=True)
    commune = models.CharField(max_length=100, default="", null=True)

    def get_full_name(self):
        return "%s %s" % (self.name, self.last_name)

    def is_admin(self):
        return self.role == "admin"
