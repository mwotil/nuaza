from Nuaza.search.models import SearchTerm
from Nuaza.pdcts.models import Product
#from Nuaza.pdcts.models import Category
from django.db.models import Q
from Nuaza.stats import stats

STRIP_WORDS = ['a','an','and','by','for','from','in','no','not',
               'of','on','or','that','the','to','with']

def store(request, q, cat):
    """ stores the search text """
    # if search term is at least three chars long, store in db
    if len(q) > 2:
        term = SearchTerm()
        term.q = q
	term.cat = None
        term.ip_address = request.META.get('REMOTE_ADDR')
        term.tracking_id = stats.tracking_id(request)
        term.user = None
        if request.user.is_authenticated():
            term.user = request.user
        term.save()
    
def products(search_text, category):
    """ get products matching the search text """
    words = _prepare_words(search_text)
    products = Product.active.all()
    results = {}

    if category == "":
       for word in words:
        products = products.filter(Q(product_name__icontains=word) |
        Q(description__icontains=word) |
        Q(brand__icontains=word))
        results['products'] = products
    
    else:
       for word in words:
        products = products.filter(Q(product_name__icontains=word) &
        Q(product_category__id__icontains=category) )
        results['products'] = products

    return results
    
def _prepare_words(search_text):
    """ strip out common words, limit to 5 words """
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
    return words[0:5]

def products_search(search_text):
    """ get products matching the search text """
    words = _prepare_words(search_text)
    products = Product.active.all()
    results = {}
    for word in words:
        products = products.filter(Q(product_name__icontains=word) |
        Q(description__icontains=word) |
        Q(brand__icontains=word))
        results['products'] = products
    return results

