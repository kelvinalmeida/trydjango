from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_veiw(request):
    obj = Product.objects.get(id=1)

    # my_ctx = {
    #     "title": obj.title,
    #     "description": obj.description,
    #     "price": obj.price,
    #     "summary": obj.sumary,
    # }

    my_ctx = {
        "object": obj,
    }

    return render(request, "products/product_detail.html", my_ctx)