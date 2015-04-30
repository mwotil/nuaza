from django.shortcuts import render_to_response
from django.template import RequestContext
from Nuaza.cart import cart
from Nuaza.checkout import checkout
from django.http import HttpResponseRedirect

def show_cart(request, template_name="cart/cart.html"):
	if request.method == 'POST':
		postdata = request.POST.copy()
		if postdata['submit'] == 'Remove':
			cart.remove_from_cart(request)
		if postdata['submit'] == 'Update':
			cart.update_cart(request)
   		if postdata['submit'] == 'Checkout':
			checkout_url = checkout.get_checkout_url(request)
   			return HttpResponseRedirect(checkout_url)
      
	cart_items = cart.get_cart_items(request)
	page_title = 'Shopping Cart'
	cart_subtotal = cart.cart_subtotal(request)

	return render_to_response(template_name, locals(),context_instance=RequestContext(request))

