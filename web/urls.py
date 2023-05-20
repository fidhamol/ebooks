from django.contrib import admin
from django.urls import path
from . import views
app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("shoplist", views.shoplist, name="shoplist"),
    path("login", views.login1, name="login"),
    path("signup",views.register_1,name="signup"),
    path("shop-detail", views.detail, name="shop-detail"),
]