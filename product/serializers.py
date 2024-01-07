from rest_framework import serializers
from account.serializers import UserSerializer
from home.serializers import ReviewsSerializer
from .models import Catalog, SubCatalog, Material, Compound, Product, Images, Parameter, ProductReview


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'
        read_only_fields = '__all__'


class SubCatalogSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer(read_only=True)

    class Meta:
        model = SubCatalog
        fields = '__all__'
        read_only_fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        read_only_fields = '__all__'


class CompoundSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = Compound
        fields = '__all__'
        read_only_fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Images
        fields = '__all__'
        read_only_fields = '__all__'


class ParameterSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Parameter
        fields = '__all__'
        read_only_fields = '__all__'


class ProductReviewSerializer(ReviewsSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductReview
        fields = '__all__'
        read_only_fields = ['is_bought']
