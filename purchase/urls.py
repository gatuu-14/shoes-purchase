from django.contrib import admin
from django.urls import path
from purchase import views

urlpatterns = [
    path("",views.index, name = 'home'),
    path("home",views.index, name = 'home'),
    path("about",views.about,name = 'about'),
    path("shoes", views.shoes, name= "shoes"),
    path("register", views.register, name="register"),
    path("signin", views.signin, name="signin"),
    path("signout",views.signout,name = "signout"),
    path("bill",views.order,name = "bill"),
    path("contact",views.contact,name = 'contact'),
    path("shoes",views.Order,name = 'shoes'),
    
    # path("bill", views.bill, name="bill"),

    ]