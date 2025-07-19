from django.shortcuts import render
from .models import Categories, Products


def home(request):
    shoes = Products.objects.filter(category__name = "Shoes")
    sunglasses = Products.objects.filter(category__name = "Sunglasses")
    camera = Products.objects.filter(category__name = "Camera")
    context = {
        "shoes": shoes,
        "sunglasses": sunglasses,
        "camera": camera
    }
    return render(request, 'index.html', context)



def details(request, pk):
    product = Products.objects.get(id = pk)
    return render(request, 'details.html', {'product': product})

def search(request):
    q = request.GET["query"]
    products = Products.objects.filter(name__icontains = q)
    return render(request, 'search.html', {"products": products, "q": q})