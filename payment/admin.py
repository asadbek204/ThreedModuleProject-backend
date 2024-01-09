from django.contrib import admin
from .models import *

admin.site.register(Wallet)
admin.site.register(Card)
admin.site.register(Order)
admin.site.register(Payment)
