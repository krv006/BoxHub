from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveAPIView

from apps.models import Product, Category
from apps.serializers import ProductModelSerializer, CategoryModelSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
