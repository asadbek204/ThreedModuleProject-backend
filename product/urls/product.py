from django.urls import path
from product.views.product import *

urlpatterns = [
    path('', SubCatalogView.as_view(), name='sub_catalog'),
    path('detail-<int:p_id>/', ProductView.as_view(), name='product_detail'),
    path('reviews-<int:p_id>/', ReviewView.as_view(), name='reviews'),
    path('reviews-<int:p_id>/<int:r_id>/', ReviewView.as_view(), name='review'),
]
