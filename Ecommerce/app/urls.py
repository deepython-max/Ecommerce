from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('bestseller', views.bestseller,name='bestseller'),
    path('cart', views.cart, name='cart'),
    path('cheackout', views.cheackout, name='cheackout'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('contact/', views.contact, name='contact'),
    path('shop', views.shop,name='shop'),
    path('single', views.single, name='single'),
    path('404', views.error_404, name='404'),
    path('Registration/', views.registration, name='register'),
    path('login/', views.loginUser,name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('category', views.category, name='category'),
    path('search_item', views.search_item, name='search_item'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-cart/<int:id>/', views.remove_cart, name='remove_cart'),
    # path('remove-cart/<int:id>/', views.minus_cart, name='minus_cart'),
    # path('remove-cart/<int:id>/', views.plus_cart, name='plus_cart'),
    # path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('plus-cart/<int:id>/', views.plus_cart, name='plus_cart'),
    path('minus-cart/<int:id>/', views.minus_cart, name='minus_cart'),
  

]