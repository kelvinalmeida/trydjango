from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_veiw(request):
    obj = Product.objects.get(id=1)

    my_ctx = {
        "title": obj.title,
        "description": obj.description,
        "price": obj.price,
        "summary": obj.sumary,
    }

    return render(request, "product/detail.html", my_ctx)