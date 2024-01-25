from rest_framework import generics

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

class SupplierAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CategoryAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


