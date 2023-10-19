from django.urls import path
from .views import product_detail_veiw, product_create_veiw, product_delete_veiw, product_list_veiw

app_name = 'products'
urlpatterns = [
    path('create/', product_create_veiw),
    path('<int:id>/', product_detail_veiw, name="product_detail"),
    path('', product_list_veiw),
    path('<int:id>/delete', product_delete_veiw),
]
