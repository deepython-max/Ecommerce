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
    path('404', views.error_404, name='404'),
    path('Registration/', views.registration, name='register'),
    path('login/', views.login,name='login'),
    path('logout/', views.logoutUser, name='logout')


]