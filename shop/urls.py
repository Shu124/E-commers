from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("",views.index,name="shophome"),
   path("About/",views.About,name="About Us"),
   path("contact/",views.contact,name="Contact Us"),
   path("Tracker",views.Tracker,name="Track"),
   path("Search",views.search,name="search"),
   path("viewproduct/<int:myid>",views.viewproduct,name="productview"),
   path("Checkout/",views.Checkout,name="Checkout")
]
