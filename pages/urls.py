from django.urls import path
from .views import index,about,blog,blog_details,contact,home,product_detail,product,shoping_cart

urlpatterns = [
    path('', index,name='index'),
    path('about', about,name='about'),
    path('blog', blog,name='blog'),
    path('blogdetail', blog_details,name='blog_details'),
    path('contact', contact,name='contact'),
    path('home', home,name='home'),
    path('productdetail', product_detail,name='product_detail'),
    path('product', product,name='product'),
    path('cart', shoping_cart,name='cart'),
] 

