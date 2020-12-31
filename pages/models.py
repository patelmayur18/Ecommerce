from django.db import models

# Create your models here.
class Primary_category(models.Model):
    """Show Primary Category"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Scondary_category(models.Model):
    """Show Secondary Category"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Color(models.Model):
    """It Show Product Variety Color"""
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.color

class Size(models.Model):
    """It Show Product Size"""
    size = models.CharField(max_length=200)

    def __str__(self):
        return self.size

class Brand(models.Model):
    """It show Brand Name"""
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand        

class Product(models.Model):
    """It show Product Details"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    price = models.CharField(max_length=10,default=0)
    discription = models.TextField()
    primary_category = models.ManyToManyField(Primary_category) 
    scondary_category = models.ForeignKey(Scondary_category,on_delete=models.CASCADE) 
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE) 
    color = models.ManyToManyField(Color,blank=True)
    size = models.ManyToManyField(Size,blank=True)
    image = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(default=0)
    is_sale = models.BooleanField(default=False)
    is_feture = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @property
    def in_stock(self):
        return self.stock > 0

