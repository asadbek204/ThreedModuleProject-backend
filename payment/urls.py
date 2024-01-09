from django.urls import path
from payment.views import *

urlpatterns = [
    path('', PaymentView.as_view(), name='payment'),
    path('card/', CardView.as_view(), name='card'),
    path('wallet/', WalletView.as_view(), name='wallet'),
    path('order/', OrderView.as_view(), name='order'),
]
