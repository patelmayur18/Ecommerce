from django.contrib import admin
from .models import Brand,Primary_category,Scondary_category,Product,Size,Color
from django.utils.html import format_html
# Register your models here.
admin.site.register(Primary_category)
admin.site.register(Scondary_category)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Brand)

class Product_admin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.image.url) )
    #Show display item
    list_display = ['id','title','price','brand','thumbnail','scondary_category','is_feture','is_sale','is_best_seller']
    #Give Clickeble links
    list_display_links = ('title','thumbnail')
    #Give Editable componet(hint:Use for only boolen value)
    list_editable = ('is_feture','is_sale','is_best_seller')
    #Give a Serch bar And Search according to given field
    search_fields = ['price__exact']
    #Give Side bar With Filter Facilities
    list_filter = ('title','price','brand')

admin.site.register(Product,Product_admin)
