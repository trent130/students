from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('product/<int:id>/<slug:slug>/', views.product, name='product'),
    path('product-list/', views.product_list, name='product_list'),
    path('product/add/', views.add_product, name='add_product'),
    path('category/', views.category, name='categories'),
    path('product-detail/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('product_list/<user_id>', views.user_products, name='user_product_list'),
    # other url patterns...
]
