from django.urls import path
from .views import SupplierAPIView, CategoryAPIView, ProductAPIView, ReviewAPIView

urlpatterns = [
    path('suppliers/',SupplierAPIView.as_view(), name='suppliers'),
    path('categories/',CategoryAPIView.as_view(), name='categories'),
    path('products/',ProductAPIView.as_view(), name='products'),
    path('reviews/',ReviewAPIView.as_view(), name='reviews'),
]