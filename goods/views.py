from django.shortcuts import render

from goods.models import Projects, Catigories

# Create your views here.


def catalog(request):

    goods = Projects.objects.all()
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_id):


    product = Projects.objects.get(id=product_id)

    context ={

        'product':product
    }

    return render(request, "goods/product.html", context=context)