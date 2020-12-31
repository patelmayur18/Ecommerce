from django.urls import path
from .views import index,about,blog,blog_details,contact,home,product_detail,product,shoping_cart,Quick_view

urlpatterns = [
    path('', index,name='index'),
    path('about', about,name='about'),
    path('blog', blog,name='blog'),
    path('blogdetail', blog_details,name='blog_details'),
    path('contact', contact,name='contact'),
    path('home', home,name='home'),
    path('productdetail/<slug>/', product_detail,name='product_detail'),
    path('quickview/<slug>/', Quick_view,name='quick_view'),
    path('product', product,name='product'),
    path('cart', shoping_cart,name='cart'),
] 

