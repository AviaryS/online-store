from django.urls import path

from api.v1.cart.views import cart_detail_view

urlpatterns = [
    path('detail/view/', cart_detail_view, name='cart-detail'),
]
