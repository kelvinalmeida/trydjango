from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, RawProdoctForm,  UpdateProdoctForm

from .models import Product

from django.http import Http404

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

    # productObj = Product.objects.get(id=1)

    initial_values = {
        'title': 'I\'m the good product'
    }

    # form = ProductForm(request.POST or None, instance=productObj)
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProductForm()

    my_ctx = {
        "form": form,
    }

    return render(request, "products/product_create.html", my_ctx)

def product_update_veiw(request):

    # if request.method == 'POST':


    # productObj = Product.objects.get(id=1)

    # form = ProductForm(request.POST or None, instance=productObj)
    form = product_update_veiw(request.POST or None)

    if form.is_valid():
        form.save()
        form = product_update_veiw()

    my_ctx = {
        "form": form,
    }

    return render(request, "products/update_product_create.html", my_ctx)


def product_detail_veiw(request, id:int):

    # obj = Product.objects.get(id=id)

    obj = get_object_or_404(Product, id=id)

    # The same as above
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404

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



def product_delete_veiw(request, id:int):

    # obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        obj.delete()

    # The same as above
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404

    my_ctx = {
        "object": obj,
    }

    return render(request, "products/product_delete.html", my_ctx)

def product_list_veiw(request):

    # obj = Product.objects.get(id=id)
    queryset = Product.objects.all()

    my_ctx = {
        "object_list": queryset,
    }

    return render(request, "products/product_list.html", my_ctx)
def product_list_veiw(request):

    # obj = Product.objects.get(id=id)
    queryset = Product.objects.all()

    my_ctx = {
        "object_list": queryset,
    }

    return render(request, "products/product_list.html", my_ctx)