from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('bestseller', views.bestseller,name='bestseller'),
    path('cart', views.cart, name='cart'),
    path('cheackout', views.cheackout, name='cheackout'),
    path('contact', views.contact, name='contact'),
    path('shop', views.shop,name='shop'),
    path('single', views.single, name='single'),

]