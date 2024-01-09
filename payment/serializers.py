from rest_framework import serializers
from .models import *
from product.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        exclude = ['user']
        write_only_fields = ['token']
        read_only_fields = ['balance']


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        exclude = ['id']
        write_only_fields = ['number', 'user']


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        exclude = ['id']
        read_only_fields = ['total', 'product']


class PaymentSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True)
    wallet = WalletSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Payment
        exclude = ['id']
        read_only_fields = ['order']

