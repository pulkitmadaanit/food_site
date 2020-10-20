from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    item_name= models.CharField(max_length=50)
    item_desc= models.CharField(max_length=50)
    item_price= models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://kuechentipps.de/wp-content/plugins/osetin-helper/assets/img/placeholder-category.png")

    def __str__(self):
        return self.item_name
    