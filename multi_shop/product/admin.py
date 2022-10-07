from django.contrib import admin
from product import models
from product.models import Size,Category,Color,Product,ProductDescription

# Register your models here.
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(ProductDescription)

