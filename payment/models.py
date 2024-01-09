from django.db.models import *
from account.models import User
from django.utils.translation import gettext_lazy as _

from product.models import Product


class Wallet(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='wallets')
    balance = PositiveIntegerField(default=0, null=True, blank=True, verbose_name=_("balance"))
    token = CharField(max_length=256, null=True, blank=True, unique=True)

    def __str__(self):
        return self.balance

    class Meta:
        verbose_name = 'wallet'
        verbose_name_plural = 'wallets'
        db_table = 'wallet'


class Card(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='cards')
    number = CharField(max_length=32, unique=True, verbose_name=_("number"))
    owner = CharField(max_length=128, verbose_name=_("owner"))
    name = CharField(max_length=32, verbose_name=_("name"))
    bank = CharField(max_length=32, verbose_name=_("bank"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'
        db_table = 'card'


class Order(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='orders')
    product = ForeignKey('product.Product', on_delete=CASCADE, verbose_name=_("product"), related_name="orders")
    quantity = PositiveSmallIntegerField(verbose_name=_("quantity"))
    total = PositiveIntegerField(verbose_name=_("total"))

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        db_table = 'order'


class Payment(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='payments')
    card = OneToOneField(Card, on_delete=DO_NOTHING, null=True, blank=True, verbose_name=_("card"), related_name="card_payments")
    wallet = OneToOneField(Wallet, on_delete=DO_NOTHING, null=True, blank=True, verbose_name=_("wallet"), related_name="wallet_payments")
    order = OneToOneField(Order, on_delete=DO_NOTHING, verbose_name=_("order"), related_name="order_payments")
    from_wallet = PositiveIntegerField(null=True, blank=True, verbose_name=_("amount from wallet"))
    from_card = PositiveIntegerField(null=True, blank=True, verbose_name=_("amount from card"))

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        db_table = 'payment'


class Cart(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='carts')
    product = OneToOneField(Product, on_delete=CASCADE, related_name='carts')
    amount = PositiveIntegerField(null=True, blank=True, verbose_name=_("amount"))
