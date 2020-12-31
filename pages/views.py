from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def blog_details(request):
    return render(request,'pages/blog-detail.html')  

def blog(request):
    return render(request,'pages/blog.html')

def contact(request):
    return render(request,'pages/contact.html')

def index(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'pages/index.html',context)

def product_detail(request,slug):
    product = Product.objects.get(slug=slug)
    related_product = Product.objects.filter(scondary_category=product.scondary_category)
    context = {
        'product':product,
        'related_product':related_product
    }
    print("---3")
    return render(request,'pages/product-detail.html',context)

def product(request):
    return render(request,'pages/product.html')

def shoping_cart(request):
    return render(request,'pages/shoping-cart.html')

def home(request):
    return render(request,'pages/home-02.html')   


def about(request):
    return render(request,'pages/about.html')  

def Quick_view(request,slug):
    print("--2")
    product = Product.objects.get(slug=slug)
    context = {
        'product':product
    }
    print("---1")
    return render(request,'include/quick_view.html',context)  
