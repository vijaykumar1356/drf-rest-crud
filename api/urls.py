from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('products', views.productCrud, name='product-crud'),
    path('products/', views.productCrud, name='product-crud'),
    path('products/<str:uuid>', views.productCrud, name='product-crud'),
    path('products/<str:uuid>/', views.productCrud, name='product-crud'),
]
