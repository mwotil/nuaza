from django.http import HttpResponseRedirect, HttpResponse
from models import Product, Category, ProductReview, Store, StoreReview, Review_Reply, User_Reputation, SuperCategory, Transaction, Buys, Feedback, Photo
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from forms import ProductForm,ProductReviewForm, ReplyForm, TransactionForm, TransactionReplyForm, FeedbackForm, BuyNowForm, BuyReplyForm, ProductAddToCartForm, PhotoForm
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.core import serializers
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from Nuaza.accounts.models import UserProfile
from django.db import IntegrityError
from django.core.mail import send_mail, BadHeaderError
from Nuaza.stats import stats
from Nuaza.settings import PRODUCTS_PER_ROW
from Nuaza.pdcts import product_profile, review_profile
from django.core import urlresolvers
from urlparse import urlsplit 
from django.forms.util import ValidationError
from django import forms
from Nuaza.cart import cart
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from Nuaza.settings import CACHE_TIMEOUT

def index(request, template_name="index.html"):
    """ site Index Page """
    page_title = 'Index'
    if request.flavour=='full':
        return render_to_response(template_name, locals(), context_instance=RequestContext(request))
    else:
        return render_to_response("mobile/index.html", locals(), context_instance=RequestContext(request))

def product_listing(request, template_name="pdcts/pdct_listing.html"):
    """ site Index Page """
    page_title = 'Buy a Product'
    pdct_listing = Product.objects.all()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def home(request, template_name="pdcts/index.html"):
    """ site Home Page """
    page_title = 'Home'
    search_recs = stats.recommended_from_search(request)
    featured = Product.featured.filter(is_active=True)[0:PRODUCTS_PER_ROW]
    bestseller = Product.bestseller.filter(is_active=True)[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_category(request, category_slug, template_name="pdcts/category.html"):
	c = get_object_or_404(Category, slug=category_slug)
	products = c.product_set.filter(is_active=True)
	page_title = c.category_name
#	meta_keywords = c.meta_keywords
#	meta_description = c.meta_description
	return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def show_store(request, store_slug, template_name="pdcts/store.html"):
	s = get_object_or_404(Store, slug=store_slug)
	products = s.product_set.filter(is_active=True)

	page_title = s.store_name
#	meta_keywords = c.meta_keywords
#	meta_description = c.meta_description
	return render_to_response(template_name, locals(),context_instance=RequestContext(request))


def show_review(request, review_slug, template_name="pdcts/review_details.html"):
	r = get_object_or_404(ProductReview, slug=review_slug)
	page_title = r.title

	reply_reviews = Review_Reply.approved.filter(review=r).order_by('-date')
	reply_form = ReplyForm()
	return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def show_shop(request, template_name="pdcts/shop.html"):
	page_title = "Shop"
	s = SuperCategory.objects.order_by('supercategory_name')
	c = Category.objects.all()	
	
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_all_shops(request, template_name="pdcts/shops_all.html"):
	page_title = "All Stores"
	stores = Store.objects.all()

	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def show_product(request, product_slug, template_name="pdcts/product.html"):

    product_cache_key = request.path
    # try to get product from cache
    p = cache.get(product_cache_key)
    # if a cache miss, fall back on db query
    if not p:
        p = get_object_or_404(Product.active, slug=product_slug)
        # store item in cache for next time
        cache.set(product_cache_key, p, CACHE_TIMEOUT)
    product_category = p.Category.all()
    page_title = p.product_name
    # meta_keywords = p.meta_keywords
    # meta_description = p.meta_description
    # evaluate the HTTP method, change as needed
    if request.method == 'POST':
        #create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        #create the unbound form. Notice the request as a keyword argument
        form = ProductAddToCartForm(request=request, label_suffix=':')
    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set test cookie to make sure cookies are enabled
    request.session.set_test_cookie()
    stats.log_product_view(request, p)
    # product review additions
    product_reviews = ProductReview.approved.filter(product=p).order_by('-date')
    store_reviews = StoreReview.objects.filter(product = p).order_by('rating_votes')[:3]
    reputation = User_Reputation.objects.get(user=p.user)
    user_rep = reputation.reputation*100
    votes = reputation.votes

    review_form = ProductReviewForm()
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


"""	p = get_object_or_404(Product, slug=product_slug, is_active=True)
	product_category = p.Category.all()

#	product_store = p.Store.all()
	page_title = p.product_name

	stats.log_product_view(request, p)

	product_reviews = ProductReview.approved.filter(product=p).order_by('-date')

	store_reviews = StoreReview.objects.filter(product = p).order_by('rating_votes')[:3]

	reputation = User_Reputation.objects.get(user=p.user)

	user_rep = reputation.reputation*100
	votes = reputation.votes	

	review_form = ProductReviewForm()
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
"""

""" view for each product page """

@login_required
def transact(request, product_slug, template_name="pdcts/transact.html"):
	page_title = "Bid Product"

	pdct = get_object_or_404(Product, slug=product_slug)
	offers = Transaction.objects.filter(product__slug=product_slug).order_by('-bid_price')[:1]

	if request.method =='POST':
		form = TransactionForm (request.POST)
		p = get_object_or_404(Product, slug=product_slug)
		
		email_subject = 'Approve a buyer Offer'
		email_body = "Hello %s, \n\nThis is a My Campuser seller alert send to the Site's Sellers. \n\nPlease, check your My Campuser transactions page to either Accept or Reject a new buyer offer for the product %s by using the following link: \n\nhttp://mycampuser.com/accounts/my_transactions/ \n\nRegards,\nMy Campuser Team" % (p.user, p.product_name) 

		if form.is_valid():

			r = form.cleaned_data["quantity"]

			if r > p.quantity:
#				raise forms.ValidationError('%s is only available. Request for it or less' % (p.quantity))
				qtty = "Available: %d . Enter it or Less." % (p.quantity) 
				form = BuyNowForm()
			else:

				buy = form.save(commit=False)
				buy.user = request.user
				buy.product = p
				buy.status = "Not Yet Approved"
				buy.save()
				send_mail(email_subject, email_body, 'sales@mycampuser.com', [p.user.email])

				return HttpResponseRedirect('/accounts/my_transactions/')
	else:
		p = get_object_or_404(Product, slug=product_slug)
		form = TransactionForm()
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))

@login_required
def buy_now(request, product_slug, template_name="pdcts/buy-now.html"):
	page_title = "Buy Product"

	if request.method =='POST':
		form = BuyNowForm (request.POST)
		p = get_object_or_404(Product, slug=product_slug)
		
		email_subject = 'Approve a buyer Offer'
		email_body = "Hello %s, \n\nThis is a My Campuser seller alert send to the Site's Sellers. \n\nPlease, check your My Campuser transactions page to either Accept or Reject a new buyer offer for the product %s. You can follow the link below: \n\nhttp://mycampuser.com/accounts/my_transactions/\n\nRegards,\n\nMy Campuser Team" % (p.user, p.product_name) 

		if form.is_valid():

			#This is the required quantity
			r = form.cleaned_data["quantity"]

			if r > p.quantity:
#				raise forms.ValidationError('%s is only available. Request for it or less' % (p.quantity))
				qtty = "Available: %d . Enter it or Less." % (p.quantity) 
				form = BuyNowForm()

			else:

				buy = form.save(commit=False)
				buy.user = request.user
				buy.product = p
				buy.status = "Not Yet Approved"
				buy.price = p.price
				buy.save()
				send_mail(email_subject, email_body, 'sales@mycampuser.com', [p.user.email])

				return HttpResponseRedirect('/accounts/my_transactions/')
	else:
		p = get_object_or_404(Product, slug=product_slug)
		form = BuyNowForm()
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))




@login_required
def rate_user(request, product_slug, template_name="pdcts/rate_user.html"):
	page_title = "Rate User"
	if request.method =='POST':
		form = FeedbackForm (request.POST)
		p = get_object_or_404(Product, slug=product_slug)

		check = Feedback.objects.filter(user=request.user, product=p)
		own_check = Feedback.objects.filter(user=p.user)

		if form.is_valid():

			if check or own_check:
				chck = "You can only rate this user once for this Product" 
				own_chck = "You can't rate yourself" 
				form = FeedbackForm()

			else:

				rate = form.save(commit=False)
				rate.user = request.user
				rate.product = p
				rate.save()
			
				reputation = User_Reputation.objects.filter(user = p.user)

				if reputation:
					r = User_Reputation.objects.get(user = p.user)

					alpha = rate.rating

					beta = 1 - alpha
					repute = r.reputation
					entity_alpha = r.entity_alpha
					entity_beta =  r.entity_beta
					votes = r.votes
					entity_alpha += alpha
					entity_beta += beta
					votes += 1
					entity_reputation = (entity_alpha/(entity_alpha + entity_beta))

					new_repute = (repute + entity_reputation)/2

					r.reputation = new_repute
					r.votes = votes
					r.entity_alpha = entity_alpha
					r.entity_beta = entity_beta
					r.save()

				


				else:
					r = User_Reputation()
					r.user = p.user
					r.reputation = 0.5
					r.entity_alpha = 0.5
					r.entity_beta = 0.5
					r.votes = 0
					r.save()


			


				return HttpResponseRedirect('/home/')
	

	else:
		form = FeedbackForm()
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))




@login_required
def reply_transact(request, transaction_id, template_name="pdcts/reply_transact.html"):
	page_title = "Bid Reply"
	if request.method =='POST':
		form = TransactionReplyForm (request.POST)
		t = get_object_or_404(Transaction, transact_id=transaction_id)

		status = request.POST.get('status')

		email_subject = 'Bid Offer Approved'
		email_body = "Hello %s, \n\nThis is a My Campuser buyer alert send to the Site's Buyers. \n\nPlease, check your My Campuser transactions page. There is seller approval on your offer for the commodity %s.\n\nIf your offer has been rejected, then you can make another more improved one otherwise you can now contact the Seller by following the link below: \n\nhttp://mycampuser.com/accounts/my_transactions/ \n\nRegards,\n\nMy Campuser Team" % (t.user, t.product) 

		if form.is_valid():
#			bid_reply = form.save(commit=False)
			t.status = status
			t.save()
			send_mail(email_subject, email_body, 'sales@mycampuser.com', [t.user.email])

#			return HttpResponseRedirect('/transaction_success/')
			return HttpResponseRedirect('/accounts/my_transactions/')
	else:
		form = TransactionReplyForm()
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))

@login_required
def reply_buy(request, buy_id, template_name="pdcts/reply_buy.html"):
	page_title = "Seller Reply"
	if request.method =='POST':
		form = BuyReplyForm (request.POST)
		b = get_object_or_404(Buys, buy_id=buy_id)

		status = request.POST.get('status')

		email_subject = 'Buy Offer Approved'
		email_body = "Hello %s, \n\nThis is a My Campuser buyer alert send to the Site's Buyers. \n\nPlease, check your My Campuser transactions page. There is seller approval on your offer for the commodity %s.\nIf your offer has been rejected, then you can search for other products or wait for the next offer. \n\nIf the offer has been accepted, follow the link http://mycampuser.com/accounts/my_transactions/ to contact the seller.\n\nRegards,\nMy Campuser Team" % (b.user, b.product) 

		if form.is_valid():
#			bid_reply = form.save(commit=False)
			b.status = status
			b.save()
			send_mail(email_subject, email_body, 'sales@mycampuser.com', [b.user.email])

#			return HttpResponseRedirect('/transaction_success/')
			return HttpResponseRedirect('/accounts/my_transactions/')
	else:
		form = BuyReplyForm()
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))




def transaction_success (request):
	page_title = 'Successful Transaction'
	return render_to_response('transaction_success.html', locals(), context_instance = RequestContext(request))

def help (request):
	page_title = 'Help'
	return render_to_response('help.html', locals(), context_instance = RequestContext(request))

def success (request):
	page_title = 'Success'
	return render_to_response('success.html', locals(), context_instance = RequestContext(request))

def success_del (request):
	page_title = 'Delete Success'
	return render_to_response('success_del.html', locals(), context_instance = RequestContext(request))

def profile_required(func):
    """View decorator that redirects users to the create profile page if they
haven't yet to create their profile. Implies (and applies) login_required.

"""
    def decorator(request, *args, **kwargs):
        if UserProfile.objects.filter(user=request.user).exists():
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/accounts/profile_info/')
    return login_required(decorator)



@profile_required
def add_product (request, template_name="pdcts/add.html"):
        request.breadcrumbs(("Submit a Product"),request.path_info)
	page_title = 'Submission'

    	'''try:
        	profile = request.user.get_profile()
    	except UserProfile.DoesNotExist:
       		profile = UserProfile(user=request.user)
        	profile.save() '''

	if request.method =='POST':
		form = ProductForm (request.POST, request.FILES)

		email_subject = 'Approve a Product'
		email_body = "Hello Administrator, \n\nThis is a My Campuser alert for products that have been submitted and are awaiting your approval.\n\nLogin to the admin panel to activate/approve these products\n\nRegards,\nMy Campuser Team"

		if form.is_valid():
			add = form.save(commit=False)
			add.user = request.user
			product_name = request.POST.get('product_name')
			add.product_name = product_name.title()
			add.save()
			form.save_m2m()
			send_mail(email_subject, email_body, 'sales@mycampuser.com' , ['admin@mycampuser.com'])

	             	reputation = User_Reputation.objects.filter(user = request.user)

	             	if reputation:
				r = User_Reputation.objects.get(user = request.user)
				nR = r.reputation
	              	else:
		   		r = User_Reputation()
		              	r.user = request.user
		             	r.reputation = 0.5
		                r.entity_alpha = 0.5
		               	r.entity_beta = 0.5
		               	r.votes = 0
		               	r.save()                        

			return HttpResponseRedirect('/success/')
	else:
		form = ProductForm()
	return render_to_response(template_name, locals(), context_instance = RequestContext(request))


@login_required
def delete (request):
	if request.POST.get('delete'):
		slug = request.POST.get('slug')
   		pdct = Product.objects.get(slug = slug)

		subject = pdct.product_name
		message = 'Delete the Above Product. The Submitter has Suggested'
		from_email = request.user.email

		if subject and message and from_email:
		        try:
				send_mail(subject, message, from_email, ['support@mycampuser.com'])
        		except BadHeaderError:
            			return HttpResponse('Invalid header found.')
			return HttpResponseRedirect('/success_del/')

@login_required
def add_review(request):
#    review_check = ProductReview.objects.filter
    form = ProductReviewForm(request.POST)

    if form.is_valid():
        review = form.save(commit=False)
        slug = request.POST.get('slug')
	store = request.POST.get('Store')

	reputation = User_Reputation.objects.filter(user = request.user)
	product = Product.objects.get(slug=slug)

	if reputation:
		r = User_Reputation.objects.get(user = request.user)
		repute = r.reputation
	else:
		r = User_Reputation()
		r.user = request.user
		r.reputation = 0.5
		r.entity_alpha = 0.5
		r.entity_beta = 0.5
		r.votes = 0
		repute = 0.5
		r.save()

	review.rating = (review.rating * repute)	

	if repute == 0:
		product.rating_votes = 0	

	else:
		str_ve = Store.objects.get(store_name = review.Store)

		str_ve.rating_votes += 1
		str_ve.rating_score += review.rating
		str_ve.save()

		product.rating_votes += 1
		product.rating_score += review.rating
		product.save()	

		store_rev = StoreReview.objects.filter(store = review.Store, product = product)


		if store_rev:
			st_rev = StoreReview.objects.get(store = store, product = product)
			st_rev.rating_votes += 1
			st_rev.rating_score += review.rating
			st_rev.save()
		else:

			p = StoreReview()
			p.rating_votes = 1
			p.rating_score = review.rating
			p.product = product
			p.store = str_ve
			p.save()

	review.user = request.user
        review.product = product
	review.save()
    
        template = "pdcts/test.html"
        html = render_to_string(template, {'review': review })
        response = simplejson.dumps({'success':'True', 'html': html})
        
    else:
        html = form.errors.as_ul()
        response = simplejson.dumps({'success':'False', 'html': html})
    return HttpResponse(response, content_type='application/javascript; charset=utf-8')



@login_required
def add_reply(request):
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        review = request.POST.get('review')
        user_rep = request.POST.get('user')
	r1 = reply.rate_objective
	r2 = reply.rate_complete

	repute_rev = User_Reputation.objects.get(user = user_rep)

	reputation = User_Reputation.objects.filter(user = request.user)

	if reputation:
		r = User_Reputation.objects.get(user = request.user)
		repute = r.reputation
		entity_alpha = r.entity_alpha
		entity_beta =  r.entity_beta
	else:
		r = User_Reputation()
		r.user = request.user
		r.reputation = 0.5
		r.entity_alpha = 0.5
		r.entity_beta =  0.5
		r.votes = 0

		entity_alpha = 0.5
		entity_beta = 0.5
		repute = 0.5

		r.save()

	#r3 = ((r1+r2)/2) * repute/1000

	alpha = ((r1+r2)/2)

        beta = 1 - alpha
        entity_alpha += alpha
        entity_beta += beta
	entity_reputation = (entity_alpha/(entity_alpha + entity_beta))


	r4 = repute_rev.reputation

	if r4 == 1:
		repute_rev.reputation = r4
		repute_rev.entity_alpha = entity_alpha
		repute_rev.entity_beta = entity_beta
	 	repute_rev.save()

	else:
		repute_rev.reputation = (r4 + entity_reputation)/2
		repute_rev.entity_alpha = entity_alpha
		repute_rev.entity_beta = entity_beta
	 	repute_rev.save()

        review = ProductReview.objects.get(id=review)
	reply.review = review
        reply.user = request.user
	
	reply.save()
    
        template = "pdcts/reply_review.html"
        html = render_to_string(template, {'reply': reply })
        response = simplejson.dumps({'success':'True', 'html': html})
        
    else:
        html = form.errors.as_ul()
        response = simplejson.dumps({'success':'False', 'html': html})
    return HttpResponse(response, content_type='application/javascript; charset=utf-8')


@login_required
def product_info(request, product_slug, template_name="pdcts/poduct_edit.html"):
#    request.breadcrumbs( ( ("My Account", '/accounts/my_account/'), ("Edit Profile", request.path_info) ) )
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_profile.set(request, product_slug)
            url = urlresolvers.reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        pdct_profile = product_profile.retrieve(request, product_slug)
        form = ProductForm(instance=pdct_profile)
    page_title = 'Edit Product Information'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def review_info(request, review_slug, template_name="pdcts/review_edit.html"):
#    request.breadcrumbs( ( ("My Account", '/accounts/my_account/'), ("Edit Profile", request.path_info) ) )
    if request.method == 'POST':
        form = ProductReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review_profile.set(request, review_slug)
            url = urlresolvers.reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        rev_profile = review_profile.retrieve(request, review_slug)
        form = ProductReviewForm(instance=rev_profile)
    page_title = 'Edit Review Information'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))



@csrf_exempt
@login_required
def upload_photo(request):

    form=PhotoForm(request.POST,request.FILES)

    if request.method=='POST':
        if form.is_valid():
           name = request.POST['product_name']
           desc = request.POST['product_desc']
           image = request.FILES['uploaded']

           new_image = Photo(title=name,photo=image,description=desc)

           new_image.save()
           #response for testing purposes
           sResponse={"SUCCESS": "1", "MESSAGE": "Upload was Successfull"}
           return HttpResponse(simplejson.dumps(sResponse), content_type='application/json')
    sResponse={"SUCCESS": "0", "MESSAGE": "Upload was Not Successfull"}
    return HttpResponse(simplejson.dumps(sResponse), content_type='application/json')
