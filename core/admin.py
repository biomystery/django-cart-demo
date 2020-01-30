from django.contrib import admin
from core.models import UserProfile, Product, Category
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Category)
