from rest_framework import viewsets

from .models import (
    Supplier,
    Category,
    Product,
    Review,
)

from .serializers import (
    SupplierSerializer,
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
)


class SupplierAPIView(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewAPIView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


