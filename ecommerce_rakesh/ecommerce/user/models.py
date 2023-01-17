from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
import datetime

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print("instance===", instance)

AddressType = (("Home","Home"),
               ("Office","Office"),
               ("Other","Other"))

class AddressTable(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    addressId = models.AutoField(primary_key= True)
    addressType = models.CharField(max_length=100,choices=AddressType,default="Home")
    address = models.TextField()
    nikeName = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nikeName)

OrderStatusType = (("pending","pending"),
               ("Conform","Conform"))

class OrderTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderId = models.CharField(max_length=100,primary_key=True)
    orderData = models.TextField()
    totalAmount = models.FloatField()
    status = models.CharField(max_length=100,default="pending",choices=OrderStatusType)

    def __str__(self):
        return str(self.orderId)


class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class SubCategory(models.Model):
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCategoryId = models.AutoField(primary_key=True)
    subCategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.subCategoryName


class Product(models.Model):
    subCategoryId = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    productId = models.CharField(max_length=100,primary_key=True)
    productName = models.CharField(max_length=100)
    productPrice = models.FloatField()
    productDescription = models.TextField()
    brand = models.CharField(max_length=500)
    productImage = models.CharField(max_length=500)
    productImage1 = models.CharField(max_length=500)
    productImage2 = models.CharField(max_length=500)
    productImage3 = models.CharField(max_length=500)
    productImage4 = models.CharField(max_length=500)
    productImage5 = models.CharField(max_length=500)
    TodayDeals = models.BooleanField(default=False)
    frequentlyPurchase = models.BooleanField(default=False)
    TopRate = models.BooleanField(default=False)
    BestSeller = models.BooleanField(default=False)

    def __str__(self):
        return self.productName

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profileId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100,default='',null=True)
    email = models.CharField(max_length=100, default='',null=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wishlistId = models.AutoField(primary_key=True)
    wishlistData = models.TextField()
    status = models.CharField(max_length=1,default="0")

    def __str__(self):
        return str(self.wishlistId)


class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    AddToCartId = models.AutoField(primary_key=True)
    AddToCartData = models.TextField()
    status = models.CharField(max_length=1,default="0")

    def __str__(self):
        return str(self.AddToCartId)




class RatingAndReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderId = models.ForeignKey(OrderTable,on_delete=models.CASCADE)
    ratingId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    rating = models.FloatField()
    review = models.CharField(max_length=1000)

    def __str__(self):
        return self.productName



class ProductDetail(models.Model):
    productId = models.ForeignKey(Product,on_delete=models.CASCADE)
    productFeature = models.TextField()

    def __str__(self):
        return self.productId



class viewEvevnt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    viewId = models.AutoField(primary_key= True)
    dateTime = models.DateTimeField(default=datetime.datetime.now())








