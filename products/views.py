from django.shortcuts import render
from .forms import ProductForm, RawProdoctForm
from .models import Product

# Create your views here.

# def product_create_veiw(request):
    
#     my_form = RawProdoctForm(initial=initial_values)
    
#     if request.method == 'POST':
#         my_form = RawProdoctForm(request.POST)
#         if my_form.is_valid():
#             # the data is good 
#             print(my_form.cleaned_data)
            
#             # dicionário transformado em argumentos usando **
#             Product.objects.create(**my_form.cleaned_data)

#     my_ctx = {
#         "form": my_form
#     }
#     return render(request, "products/product_create.html", my_ctx)

# def product_create_veiw(request):
#     # print(request.GET)
#     # print(request.POST)

#     if( request.method == 'POST'):
#         title = request.POST['title']
#         print(title)
#         print('Fiz POST')
#     if( request.method == 'GET'):
#         title = request.GET['title']

#         print(title)
#         print('Fiz GET')

    # my_ctx = {}
    # return render(request, "products/product_create.html", my_ctx)


def product_create_veiw(request):

    productObj = Product.objects.get(id=1)

    initial_values = {
        'title': 'I\'m the good product'
    }

    form = ProductForm(request.POST or None, instance=productObj)

    if form.is_valid():
        form.save()
        form = ProductForm()

    my_ctx = {
        "form": form,
    }

    return render(request, "products/product_create.html", my_ctx)

def product_detail_veiw(request, id:int):
    obj = Product.objects.get(id=id)

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