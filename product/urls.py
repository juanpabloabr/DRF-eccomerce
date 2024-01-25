# from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import SupplierAPIView, CategoryAPIView, ProductAPIView, ReviewAPIView


router = SimpleRouter()
router.register('suppliers', SupplierAPIView)
router.register('categories', CategoryAPIView)
router.register('products', ProductAPIView)
router.register('reviews', ReviewAPIView)


