from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    product_desc = models.CharField(max_length=300)
    category = models.CharField(max_length=300, default="")
    subcategory = models.CharField(max_length=300, default="")
    price = models.IntegerField(default=0)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='gou/image', default="")

    def __str__(self):
        return (f"{self.product_name}")


class Contact(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=70, default='')
    phone = models.CharField(max_length=10, default='')
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return (f"{self.name}")
