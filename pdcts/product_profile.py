from Nuaza.pdcts.models import Product
from Nuaza.pdcts.forms import ProductForm

def retrieve(request, product_slug):
    try:
        profile = Product.objects.get(user=request.user, slug=product_slug)
    except Product.DoesNotExist:
        profile = Product(user=request.user)
#        profile.save()
    return profile
    
def set(request, product_slug):
    """ updates the information stored in the user's profile """
    profile = retrieve(request, product_slug)
    profile_form = ProductForm(request.POST, request.FILES, instance=profile)
    profile_form.save()
    
