from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('signup/', views.userSignup.as_view()),
    path('login/', obtain_auth_token, name='login'),

    #address
    path('postAddress/', views.PostaddressData.as_view()),
    path('getAddress/', views.getAddressData.as_view()),
    path('getAddressID/<addressId>/', views.getAddressDataID.as_view()),
    path('postAddressDelete/', views.postAddressDelete.as_view()),
    path('updateAddress/', views.updateAddress.as_view()),

    #orderData
    path('postOrder/', views.PostOrderData.as_view()),
    path('getOrder/', views.getOrderData.as_view()),
    path('getOrder/<status>/', views.statusOrderData.as_view()),

    #category
    path('postCategory/', views.postCategory.as_view()),
    path('getCategory/', views.getCategorys.as_view()),

    #subcategory
    path('postSubCategory/', views.postSubCategory.as_view()),
    path('getSubCategory/', views.getSubCategory.as_view()),
    path('getSubCategory/<categoryId>/', views.getSubCategory.as_view()),

    #product
    path('postProduct/', views.postProduct.as_view()),
    path('getProduct/', views.getProduct.as_view()),
    path('getProduct/<subCategoryId>/', views.getProductSubCategory.as_view()),

    #profile
    path('getProfile/', views.getProfile.as_view()),
    path('updateProfile/', views.updateProfile.as_view()),

    #wishlist
    path('postWishlist/', views.postWishlist.as_view()),
    path('StatusUpdateWishlist/', views.StatusUpdateWishlist.as_view()),
    path('getWishlist/', views.getWishlist.as_view()),
    path('DeleteWishlist/', views.DeleteWishlist.as_view()),

    #add to cart
    path('postAddToCart/', views.postAddToCart.as_view()),
    path('getAddToCart/', views.getAddToCart.as_view()),
    path('StatusUpdateCart/', views.StatusUpdateAddToCart.as_view()),
    path('DeleteAddToCart/', views.DeleteAddToCart.as_view()),

    #rating and review
    path('postRatingAndReview/', views.postRatingAndReview.as_view()),
    path('getRatingAndReview/', views.getRatingAndReview.as_view()),

    #product detail
    path('postProductDetail/', views.postProductDetail.as_view()),
    path('getProductDetail/', views.getProductDetail.as_view()),

    #search filter
    path('searchFilter/<productName>/', views.searchfilter.as_view()),

    #location
    path('locationDetail/', views.locationDetail.as_view()),

    #Today deals
    path('StatusUpdateTodayDeals/', views.StatusUpdateTodayDeals.as_view()),
    path('getTodayDeals/', views.getTodayDeals.as_view()),
    #frequentlyPurchase
    path('StatusUpdateFrequentlyPurchase/', views.StatusUpdateFrequentlyPurchase.as_view()),
    path('getFrequentlyPurchase/', views.getFrequentlyPurchase.as_view()),

    #topRated
    path('StatusUpdateTopRate/', views.StatusUpdateTopRate.as_view()),
    path('getStatusUpdateTopRate/', views.getTopRate.as_view()),

    #BestSellar
    path('StatusUpdateBestSeller/', views.StatusUpdateBestSeller.as_view()),
    path('getStatusUpdateBestSeller/', views.getBestSeller.as_view()),

    #view Event
    path('postViewEvent/', views.postViewEvent.as_view()),
    path('getViewEvent/', views.getViewEvent.as_view()),


    #Category all
    path('getCategoryAllData/', views.GetCategoryAllData.as_view()),

    path('UpdateAddToCart/', views.UpdateAddToCart.as_view()),













]