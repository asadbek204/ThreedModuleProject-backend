from rest_framework import serializers
from account.serializers import UserSerializer
from home.serializers import ReviewsSerializer
from .models import Catalog, SubCatalog, Material, Compound, Product, Images, Parameter, ProductReview, Description


class SubCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCatalog
        fields = '__all__'
        read_only_fields = ['catalog', 'name']


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = '__all__'
        read_only_fields = ['name', 'gender']


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'
        read_only_fields = ['name', 'fit']


class CompoundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compound
        exclude = ['material']
        read_only_fields = ['name', 'percentage']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['material', 'category']


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ['product']
        read_only_fields = ['image', 'is_main']


class ParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parameter
        exclude = ['product']
        read_only_fields = ['size', 'color', 'available']


class ProductReviewSerializer(ReviewsSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ProductReview
        exclude = ['product']
        read_only_fields = ['is_bought']
