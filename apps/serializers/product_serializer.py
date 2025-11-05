from rest_framework.serializers import ModelSerializer

from apps.models import Product, Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id', 'name',


class CategoryDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name', 'quantity', 'price_in', 'price_out',
            'price_discounted', 'image', 'category'
        )

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['category'] = CategoryModelSerializer(instance.category).data

        price_in = instance.price_in or 0
        price_out = instance.price_out or 0
        discount = instance.price_discounted or 0
        repr['benefit'] = price_out - price_in - discount
        return repr
