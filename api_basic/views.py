from rest_framework import viewsets
from rest_framework.response import Response

from .models import Item, Oder, Category, Customer, Oder_item
from .serializers import ItemSerializer, OrderSerializer, CustomerSerializer, CategorySerializer, OrderItemSerializer


# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        item = Item.objects.all()
        return item

    def create(self, request, *args, **kwargs):
        item_data = request.data

        new_item = Item.objects.create(category=Category.objects.get(name=item_data["category"]),
                                       name=item_data["name"], image=item_data["image"],
                                       describes=item_data["describes"], price=item_data["price"],
                                       inventory=item_data["inventory"])
        new_item.save()

        serializers = ItemSerializer(new_item)
        return Response(serializers.data)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        category = Category.objects.all()
        return category


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        customer = Customer.objects.all()
        return customer


class OderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        oder = Oder.objects.all()
        return oder

    def create(self, request, *args, **kwargs):
        oder_data = request.data

        new_oder = Oder.objects.create(customer=Customer.objects.get(username=oder_data["username"]),
                                       code=oder_data["code"], cost=oder_data["cost"],
                                       total_product=oder_data["total_product"])

        new_oder.save()

        serializers = OrderSerializer(new_oder)
        return Response(serializers.data)


class OderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        oderItem = Oder_item.objects.all()
        return oderItem

    def create(self, request, *args, **kwargs):
        oder_item_data = request.data

        new_oder_item = Oder_item.objects.create(oder=Oder.objects.get(code=oder_item_data["code"]),
                                                 item=Item.objects.get(id=oder_item_data["item_id"]),
                                                 quantity=oder_item_data["quantity"])

        old_item = Item.objects.get(id=oder_item_data["item_id"])
        if old_item.inventory >= oder_item_data["quantity"]:
            old_item.inventory -= oder_item_data["quantity"]
            old_item.save()
            new_oder_item.save()

        serializers = OrderItemSerializer(new_oder_item)
        return Response(serializers.data)
