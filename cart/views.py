from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from products.models import Product
import json


# Create your views here.
def add_to_cart(request):
    product_id = request.POST['product']
    quantity = int(request.POST['quantity'])
    
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + quantity
    request.session['cart'] = cart

    return redirect ("/")
    
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    overall_total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        total = quantity * product.price
        overall_total += total
        
    
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'brand': product.brand,
            'sku': product.sku,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'stock': product.stock,
            'quantity': quantity,
            'total': total,
        })   

    
    return render(request, "cart/view_cart.html", {'cart_items': cart_items, 'overall_total':overall_total})
    
def remove_cart_item(request):
    product_id = request.POST['product']
    
    cart = request.session.get('cart', {})
    del cart[product_id]
    request.session['cart'] = cart
    
    return redirect(view_cart)