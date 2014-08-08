from django.db import models


# Create your models here.
class resume(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_no = models.IntegerField(max_length=15)
    address = models.TextField(max_length=500)
    email_id = models.EmailField(max_length=254)
    gender = models.CharField(max_length=10)
