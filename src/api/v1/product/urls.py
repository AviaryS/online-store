from django.urls import path

from api.v1.product.views import product_list_view, product_detail_view

urlpatterns = [
    path('list/', product_list_view, name='product-list'),
    path('detail/<int:product_id>/', product_detail_view, name='product-detail'),
]
