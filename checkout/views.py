from django.shortcuts import render, get_object_or_404
from products.models import Product
from .forms import MakePaymentForm, OrderForm

# Create your views here.

def get_cart_items_and_total(cart):
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
        
        
    return { 'cart_items': cart_items, 'overall_total':overall_total }







def show_checkout(request):
    cart = request.session.get('cart', {})
    
    cart_items_and_total = get_cart_items_and_total(cart)
        
    form = MakePaymentForm()
    form2 = OrderForm()
    
    context = {'payment_form': form, 'order_form': form2}
    context.update(cart_items_and_total)
    
    return render(request, "checkout/checkout.html", context )