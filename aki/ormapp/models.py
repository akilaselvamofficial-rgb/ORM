from django.db import models
from django.contrib import admin
class Product(models.Model):
    Name=models.CharField(max_length=100)
    product_id=models.IntegerField(primary_key=True)
    Brand=models.CharField(max_length=20)
    Price=models.FloatField()
    manufacture_data=models.DateField()
    Expiry_date=models.DateField()
    warranty=models.CharField(max_length=10)
class ProductAdmin(admin.ModelAdmin):
    list_display=["Name","product_id","Brand","Price","manufacture_data","Expiry_date","warranty"]   

    

