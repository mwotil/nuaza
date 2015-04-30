from django_cron import cronScheduler, Job
from alerts.models import Request
from pdcts.models import Product
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q

STRIP_WORDS = ['a','an','and','by','for','from','in','no','not',
               'of','on','or','that','the','to','with']


def product_alert():
    """ get products matching the user request """
    # Get all user requests that are active

    requests = Request.objects.filter(is_active=True)
    products = Product.active.all()
    results = {}

    for req in requests:
	user = req.user
	products = products.filter(Q(product_name__icontains=req.product_name.split()))
        #Q(product_condition__icontains=req.product_condition) |
        #Q(product_pricing__icontains=req.product_pricing) |
        #Q(brand__icontains=word))
        results['user'] = products
    return results

def mail_alert():

	if product_alert():
		message_body = "Hi Consumer"
		try:
		    send_mail("Product Available Notification", message_body, ['sales@nuaza.com'], ['support@nuaza.com'])
        	except BadHeaderError:
            		return HttpResponse('Invalid header found.')

class ProductAlert(Job):
        """
                Cron Job that checks user requests and alerts them if they are available in the stores
        """
	# Job will run hourly
	run_every = 300

        def job(self):
		mail_alert()

cronScheduler.register(ProductAlert)
