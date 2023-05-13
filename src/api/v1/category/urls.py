from django.urls import path

from api.v1.category.views import category_list_view

urlpatterns = [
    path('list/', category_list_view, name='category-list')
]