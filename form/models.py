from django.db import models

# Create your models here.
class resume(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_no = models.IntegerField
    address = models.TextField
    email_id = models.EmailField(max_length=254)
    gender = models.BooleanField


