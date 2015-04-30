from Nuaza.pdcts.models import Category, Store, SuperCategory
from Nuaza.pdcts.models import Product
from Nuaza import settings

def Nuaza(request):
	return {
		'supercategory': SuperCategory.objects.all(),
		'category': Category.objects.all(),
		'store': Store.objects.order_by('-rating_votes')[:5],
		'latest': Product.active.order_by('-submitted_at')[:5],
		'reviewed': Product.active.order_by('-rating_votes')[:5],
		'site_name': settings.SITE_NAME,
		'meta_keywords': settings.META_KEYWORDS,	
		'meta_description': settings.META_DESCRIPTION,
		'request': request
	}

