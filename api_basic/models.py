from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    describes = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Oder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=100)
    creatDate = models.DateTimeField(auto_now_add=True)
    cost = models.FloatField(default=0)
    total_product = models.IntegerField(default=0)

    def __str__(self):
        return self.code


class Oder_item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    oder = models.ForeignKey(Oder, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
