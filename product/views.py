from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        product = self.get_object()
        serializer = ReviewSerializer(product.reviews.all(), many=True)
        return Response(serializer.data)
    
    # Needs to check if filter is working
    @action(
            methods=['get'],
            detail=False,
            url_path=r'category/(?P<category>\w+)/all',
            url_name='all',
    )
    def listProductByCategory(self, request, category=None):
        serializer = ProductSerializer(
            self.queryset.filter(category__name=category), many=True,
        )
        return Response(serializer.data)

class ReviewAPIView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


