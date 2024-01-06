from django.db.models import *
from account.models import User


class Wallet(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    balance = PositiveIntegerField(default=0, null=True, blank=True, verbose_name="balance")
    token = CharField(max_length=256, null=True, blank=True, unique=True)

    def __str__(self):
        return self.balance

    class Meta:
        verbose_name = 'wallet'
        verbose_name_plural = 'wallets'
        db_table = 'wallet'


class Card(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    number = CharField(max_length=32, unique=True, verbose_name="number")
    owner = CharField(max_length=128, verbose_name="owner")
    name = CharField(max_length=32, verbose_name="name")
    bank = CharField(max_length=32, verbose_name="bank")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'
        db_table = 'card'


class Order(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    product = ForeignKey('product.Product', on_delete=CASCADE, verbose_name="product")
    quantity = PositiveSmallIntegerField(verbose_name="quantity")
    total = PositiveIntegerField(verbose_name="total")


class Payment(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    card = OneToOneField(Card, on_delete=DO_NOTHING, null=True, blank=True, verbose_name="card")
    wallet = OneToOneField(Wallet, on_delete=DO_NOTHING, null=True, blank=True, verbose_name="wallet")
    order = OneToOneField(Order, on_delete=DO_NOTHING, verbose_name="order")
    from_wallet = PositiveIntegerField(verbose_name="amount from wallet")
    from_card = PositiveIntegerField(verbose_name="amount from card")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'
        db_table = 'payment'
