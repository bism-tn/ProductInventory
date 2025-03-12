"""
URL configuration for productinvetory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from productapp.views import AddproductView,ReadAllProductView,UpdateProductView,DeleteProductView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Product/AddProduct',AddproductView.as_view()),
    path('Product/ShowProducts',ReadAllProductView.as_view(),name="allproducts"),
    path("Product/update/<int:pk>",UpdateProductView.as_view()),
    path("Product/delete/<int:pk>",DeleteProductView.as_view()),
]

