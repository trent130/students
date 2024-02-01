from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    path('signin/', auth_views.LoginView.as_view(template_name='staticpages/account/login.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='staticpages/account/logout.html'), name='signout'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('chat/', views.chat, name='chat'),
    # path('chat/<str:room_name>/', views.room, name='room'),
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('user_login/', views.user_Login, name='user_login'),
    path('account/profile/', views.user_profile, name='user_profile'),
    # path('user_register/', views.user_register, name='user_register'),
    # path('user_profile/', views.user_profile, name='user_profile'),
    # path('user_profile_edit/', views.user_profile_edit, name='user_profile_edit'),
    # path('user_profile_delete/', views.user_profile_delete, name='user_profile_delete'),
    # path('user_profile_password/', views.user_profile_password, name='user_profile_password'),
    # path('user_profile_orders/', views.user_profile_orders, name='user_profile_orders'),
    # path('user_profile_order_details/', views.user_profile_order_details, name='user_profile_order_details'),
    # path('user_profile_products/', views.user_profile_products, name='user_profile_products'),
    # path('user_profile_product_details/', views.user_profile_product_details, name='user_profile_product_details'),
    # path('user_profile_product_edit/', views.user_profile_product_edit, name='user_profile_product_edit'),
    # path('user_profile_product_delete/', views.user_profile_product_delete, name='user_profile_product_delete'),
    # path('user_profile_product_add/', views.user_profile_product_add, name='user_profile_product_add'),
    # path('user_profile_product_add_images/', views.user_profile_product_add_images, name='user_profile_product_add_images'),
    # path('user_profile_product_add_images_delete/', views.user_profile_product_add_images_delete, name='user_profile_product_add_images_delete'),
    # path('user_profile_product_add_images_edit/', views.user_profile_product_add_images_edit, name='user_profile_product_add_images_edit'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='staticpages/account/password_reset.html'), name='password_reset'),
]
