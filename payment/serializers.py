from rest_framework import serializers
from .models import Wallet, Card, Order, Payment
from account.serializers import UserSerializer
from product.serializers import ProductSerializer


class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = '__all__'
        write_only_fields = ['token']
        read_only_fields = ['balance']


class CardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['total']


class PaymentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    card = CardSerializer(read_only=True)
    wallet = WalletSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = '__all__'

