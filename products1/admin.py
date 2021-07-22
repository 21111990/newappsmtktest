from django.contrib import admin
from . models import Productinshop,Product,dummproduts

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_id','name','price','stock','image')
class ProductinshopAdmin(admin.ModelAdmin):
    list_display = ('Product_name','image')
admin.site.register(Product,ProductAdmin)
admin.site.register(Productinshop,ProductinshopAdmin)
