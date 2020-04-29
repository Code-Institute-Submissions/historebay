from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart contents are available
    when rendering every web page of the application.
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})
    return {'cart_items': cart_items,
            'total': total, 'product_count': product_count}
    """
    Add 'cart.contexts.cart_contents',  to the 'context_processors': [..
    under TEMPLATES in the settings.py file.
    """
