from rest_framework import serializers

from .models import Item, Oder, Category, Customer, Oder_item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",

        )


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "image",
            "describes",
            "price",
            "inventory",
            "category"
        )
        depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "id",
            "name",
            "email",
            "address",
            "telephone",
            "username",
            "password"
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oder
        fields = (
            "id",
            "cost",
            "code",
            "total_product",
            "customer",
            "creatDate"
        )
        depth = 1


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oder_item
        fields = (
            "id",
            "oder",
            "item",
            "quantity"
        )
        depth = 1
