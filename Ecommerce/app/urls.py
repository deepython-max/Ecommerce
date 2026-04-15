from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('bestseller', views.bestseller),
    path('cart', views.cart),
    path('cheackout', views.cheackout),
    path('contact', views.contact),
    path('shop', views.shop),
    path('single', views.single),

]