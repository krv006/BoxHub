from django.urls import path

from apps.views import ProductListCreateAPIView, CategoryListCreateAPIView

urlpatterns = [
    path('product/', ProductListCreateAPIView.as_view(), name='product'),
    path('category/', CategoryListCreateAPIView.as_view(), name='category'),
]
