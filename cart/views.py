from django.shortcuts import render, redirect, get_object_or_404
from core.models import Products
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required

@login_required
def cartDetails(request):
    cart_items = CartItem.objects.filter(cart__user = request.user)
    total_quantity = 0
    for cart in cart_items:
        total_quantity += cart.quantity
    
    total_price = 0
    for cart in cart_items:
        total_price += cart.quantity * cart.product.price


    return render(request, 'carts.html', {'carts': cart_items, "total_quantity": total_quantity, "total_price": total_price})



@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    cart, _ = Cart.objects.get_or_create(user = request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product= product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect(cartDetails)

@login_required
def remove_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__user = request.user)
    item.delete()

    return redirect(cartDetails)

@login_required
def quantity(request, item_id):
    item =  get_object_or_404(CartItem, id=item_id, cart__user = request.user)
    action = request.POST['action']

    if action == "increase":
        item.quantity += 1
        item.save()
    elif action == "decrease":
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
    else: 
        item.delete()
    
    return redirect(cartDetails)