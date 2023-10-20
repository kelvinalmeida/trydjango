"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from pages.views import home_view, contact_view, about_view, imagem_view
from products.views import product_detail_veiw, product_create_veiw, product_delete_veiw, product_list_veiw

urlpatterns = [
    path('product/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('', home_view, name='home'),
    path('<int:id>/', about_view, name="product_detail"),
    path('contact/', contact_view, name="product_detail"),
    path('imagem/', imagem_view),
    path('admin/', admin.site.urls),
]
