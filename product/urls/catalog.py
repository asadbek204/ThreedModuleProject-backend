from django.urls import path, include
from product.views.catalog import *

urlpatterns = [
    path('', CatalogsView.as_view(), name='catalogs'),
    path('<str:gender>/', CatalogView.as_view(), name='catalog'),
    path('products/<int:pk>/', include('product.urls.product')),
    path('<str:gender>/products/<int:pk>/', include('product.urls.product'))
]
