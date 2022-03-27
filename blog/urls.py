from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
   path("",views.index1,name="bloghome"),
   path("blogpost/<int:id>",views.blogpost,name="blogpost")

]
