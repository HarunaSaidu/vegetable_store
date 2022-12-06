from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProdctForm

def home_page(request):
    products_preview = Product.objects.filter(use_as_preview=True)
    return render(request, 'index.html', {'products_preview': products_preview})

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products.html', {'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProdctForm()
    return render(request, 'product-details.html', {'product': product, 'cart_product_form': cart_product_form})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def terms(request):
    return render(request, 'terms.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')