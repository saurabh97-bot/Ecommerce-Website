"""Ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

urlpatterns = (
    path('', SliderView.as_view(), name="slider"),
    path('home', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact-us/', ContactView.as_view(), name="contact"),
    path('Nav/', NavView.as_view(), name="navbar"),
    path('All-products/', AllProductsView.as_view(), name="allproducts"),
    path('product/<slug:slug>', ProductDetailView.as_view(), name="productdetail"),
    path('add-to-cart/<int:pro_id>', AddtoCartView.as_view(), name="addtocart"),
    path('my-cart/', MyCartView.as_view(), name="mycart"),
    path('manage-cart/<int:cp_id>/', ManageCartView.as_view(), name="managecart"),
    path('empty-cart/', EmptyCartView.as_view(), name="emptycart"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),
    path('register/', CustomerRegistrationView.as_view(), name="customerregistration"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("login/", CustomerLoginView.as_view(), name="customerlogin"),
    path("profile/", CustomerProfileView.as_view(), name="customerprofile"),
    path("profile/order-<int:pk>/",CustomerOrderDetailView.as_view(),name="customerorderdetail"),
    path("search/",SearchView.as_view(),name="search")
)
