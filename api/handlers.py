from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended
from piston.utils import validate
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson

from Nuaza.api.models import AndroidProduct
from Nuaza.api.forms import AndroidProductForm

class ProductPostHandler(BaseHandler):
    """
    Authenticated entrypoint for Products.
    """
    model = AndroidProduct

    fields = ('product_name', 'slug', 'brand', 'manufacturer','price', 
              'quantity', 'submitted_at', 'description', 'is_active', 
              'is_bestseller', 'is_featured', 'user')

    @validate(AndroidProductForm, 'POST')
    def create(self, request):
        """
        Creates a new blogpost.
        """
        if not hasattr(request, "data"):
            request.data = request.POST
        attrs = self.flatten_dict(request.data)
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            post = AndroidProduct(product_name=attrs['product_name'], 
                            brand=attrs['brand'],
                            manufacturer=attrs['manufacturer'],
                            price=attrs['price'],
                            quantity=attrs['quantity'],
                            description=attrs['description'],
                            user=request.user)
            post.save()
            #return post
            sResponse={"SUCCESS": "1", "MESSAGE": "Product Upload Successful"}
            return HttpResponse(simplejson.dumps(sResponse), content_type='application/json')