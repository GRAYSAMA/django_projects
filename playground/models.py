from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)
    owner_number = models.IntegerField(null=True)
    date_maintained= models.DateField(null=True)


