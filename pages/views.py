from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def blog_details(request):
    return render(request,'pages/blog-detail.html')  

def blog(request):
    return render(request,'pages/blog.html')

def contact(request):
    return render(request,'pages/contact.html')

def index(request):
    return render(request,'pages/index.html')

def product_detail(request):
    return render(request,'pages/product-detail.html')

def product(request):
    return render(request,'pages/product.html')

def shoping_cart(request):
    return render(request,'pages/shoping-cart.html')

def home(request):
    return render(request,'pages/home-02.html')   

def about(request):
    return render(request,'pages/about.html')   