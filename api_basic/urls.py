from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import ItemViewSet, CategoryViewSet, OderViewSet, OderItemViewSet, CustomerViewSet

router: DefaultRouter = DefaultRouter()
router.register('item', ItemViewSet, basename='item')
router.register('category', CategoryViewSet, basename='category')
router.register('oder', OderViewSet, basename='oder')
router.register('oder_item', OderItemViewSet, basename='oder_item')
router.register('customer', CustomerViewSet, basename='customer')

urlpatterns = [
    url('', include(router.urls))
]
