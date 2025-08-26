from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request, category_slug = None):
    if category_slug:
        # filter products by category
        products = Product.objects.filter(category__slug=category_slug)
    else:
        # show all products
        products = Product.objects.all()
    product_count = products.count()



    context = {
        'products' : products,
        'product_count' : product_count,
    }
    return render(request,'store/store.html',context)
