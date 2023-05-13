from django.urls import path, include

urlpatterns = [
    path('product/', include('api.v1.product.urls')),
    path('category/', include('api.v1.category.urls')),
    path('cart/', include('api.v1.cart.urls')),
]
