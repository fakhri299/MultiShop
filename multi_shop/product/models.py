from distutils.command.upload import upload
from email.policy import default
from django.db import models


class Color(models.Model):
    name=models.CharField(max_length=50,null=True)
    slug=models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.slug



class Size(models.Model):
    name=models.CharField(max_length=50)
    slug=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.slug




class ProductDescription(models.Model):
    size=models.ManyToManyField(Size)
    product_code=models.IntegerField()
    color=models.ManyToManyField(Color)
    quantity=models.SmallIntegerField(default=0)
    about=models.TextField(null=True,blank=True)
    #reviews=

    def __str__(self):
        return str(self.product_code)

    

class Category(models.Model):
    name=models.CharField(max_length=50)
    photos=models.ImageField()
    slug=models.SlugField(max_length=50,unique=True)

    def __str__(self):
        return self.slug






class Product(models.Model):
    name=models.CharField(max_length=200)
    old_price=models.BigIntegerField(null=True)
    new_price=models.BigIntegerField()
    photo=models.ImageField(default='multi_shop/static/default_picture')
    category=models.ManyToManyField(Category)
    #rate=
    description=models.OneToOneField(ProductDescription,on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name
