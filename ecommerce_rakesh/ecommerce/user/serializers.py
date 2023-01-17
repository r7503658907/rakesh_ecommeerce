from rest_framework import serializers
from .models import *

class signupSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()


class AddressTableSerializer(serializers.Serializer):
    address = serializers.JSONField()
    nikeName = serializers.CharField(max_length=100)



class DeleteAddressTableSerializer(serializers.Serializer):
    addressId = serializers.IntegerField()

class UpdateAddressTableSerializer(serializers.Serializer):
    addressId = serializers.IntegerField()
    addressType=serializers.CharField(max_length=100)
    address = serializers.JSONField()

class OrderTableSerializer(serializers.Serializer):
    totalAmount = serializers.FloatField()
    orderData = serializers.JSONField()


class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=100)

class SubCategorySerializer(serializers.Serializer):
    subCategoryName = serializers.CharField(max_length=100)
    category_name = serializers.CharField(max_length=100)

class ProductSerializer(serializers.Serializer):
    subCategoryName = serializers.CharField(max_length=100)
    productName = serializers.CharField(max_length=100)
    productPrice = serializers.FloatField()
    brand = serializers.CharField(max_length=100)
    productImage = serializers.CharField(max_length=100)
    productImage1 = serializers.CharField(max_length=100)
    productImage2 = serializers.CharField(max_length=100)
    productImage3 = serializers.CharField(max_length=100)
    productImage4 = serializers.CharField(max_length=100)
    productImage5 = serializers.CharField(max_length=100)
    productDescription = serializers.JSONField()
    TodayDeals = serializers.BooleanField(required=False)
    frequentlyPurchase = serializers.BooleanField(required=False)
    TopRate = serializers.BooleanField(required=False)
    BestSeller = serializers.BooleanField(required=False)


class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mobile = serializers.CharField(required=False)
    email = serializers.CharField(required=False)
    password = serializers.CharField(max_length=100)


class UpdateProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    password = serializers.CharField(max_length=100)

class WishlistSerializer(serializers.Serializer):
    wishlistData = serializers.JSONField()

class StatusUpadateWishlistSerializer(serializers.Serializer):
    wishlist = serializers.IntegerField()
    status=serializers.CharField(max_length=1)

class AddToCartSerializer(serializers.Serializer):
    AddToCartData = serializers.JSONField()

class StatusUpadateAddToCartSerializer(serializers.Serializer):
    AddToCartId = serializers.IntegerField()
    status=serializers.CharField(max_length=1)

class StatusDeleteAddToCartSerializer(serializers.Serializer):
    AddToCartId = serializers.IntegerField()

class StatusDeleteWishlistIdSerializer(serializers.Serializer):
    wishlistId = serializers.IntegerField()


class RatingAndReviewSerializer(serializers.Serializer):
    productName = serializers.CharField(max_length=100)
    rating = serializers.IntegerField()
    review = serializers.CharField(max_length=1000)

class ProductDetailSerializer(serializers.Serializer):
    productId= serializers.CharField(max_length=100)
    productFeature = serializers.JSONField()

class LocationDetailSerializer(serializers.Serializer):
    Latitude = serializers.CharField(max_length=100)
    Longitude = serializers.CharField(max_length=100)


class StatusUpadateTodayDeals(serializers.Serializer):
    productId = serializers.CharField(max_length=100)
    TodayDeals=serializers.BooleanField()

class StatusUpadateFrequentlyPurchase(serializers.Serializer):
    productId = serializers.CharField(max_length=100)
    frequentlyPurchase=serializers.BooleanField()

class StatusUpadateTopRated(serializers.Serializer):
    productId = serializers.CharField(max_length=100)
    TopRate=serializers.BooleanField()

class StatusUpadateBestSeller(serializers.Serializer):
    productId = serializers.CharField(max_length=100)
    BestSeller=serializers.BooleanField()

class viewEventSerializer(serializers.Serializer):
    productId = serializers.CharField(max_length=100)