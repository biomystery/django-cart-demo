from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})
    #this is the default product class
class Product(models.Model):
    name = models.CharField(max_length=50)
    price_ht = models.FloatField()
    category = models.ForeignKey("core.Category", on_delete=models.CASCADE, related_name='products')
    TVA_AMOUNT = 0.0725
    def price_ttc(self):
        return self.price_ht + self.TVA_AMOUNT
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})
