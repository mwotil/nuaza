from models import ProductReview, Product, Store, Review_Reply, Transaction, Feedback, Buys, Category, Photo
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, render_to_response
from django import forms
from django.contrib.comments.forms import CommentForm
from django.db.models import Q
from widgets import StarsRadioFieldRenderer, StarsRadioInput
from stdimage import StdImageField
from django.template import RequestContext
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from marcofucci_utils import fields as marcofucci_fields
from tekextensions.widgets import SelectWithPopUp, MultipleSelectWithPopUp
from django.utils.safestring import mark_safe

RATING_CHOICES = ((1,1),(2,2),(3,3),(4,4),(5,5),)
USER_RATING_CHOICES = ((0.2,0.2),(0.4,0.4),(0.6,0.6),(0.8,0.8),(1,1),)
REPLY_CHOICES = (
    ('', '--------------'),
    ('Accepted', 'Accept'),
    ('Rejected', 'Reject'),
    ('Not Yet Approved', 'Not Approve'),
)

TYPE_CHOICES = (
#    ('', '--Select the Product Type--'),
    ('Review', 'Review'),
    ('Sale', 'Sale'),
)

CONDITION_CHOICES = (
#    ('', '--Select Product Condition--'),
    ('New', 'New'),
    ('Used', 'Used'),
)

PRICING_CHOICES = (
#    ('', '--Select Pricing Options--'),
    ('Fixed', 'Fixed'),
    ('Negotiable', 'Negotiable'),
)

class HorizRadioRenderer(forms.RadioSelect.renderer):
    """ this overrides widget method to put radio buttons horizontally
        instead of vertically.
    """
    def render(self):
            """Outputs radios"""
            return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

class ProductReviewForm(forms.ModelForm):
#	captcha = CaptchaField()
#	recaptcha = marcofucci_fields.ReCaptchaField()

# 	p = get_object_or_404(Product, slug=product_slug)
#	product_store = p.product_store.all()

	Store = forms.ModelChoiceField(Store.objects.all(), widget=SelectWithPopUp)

	def __init__(self, *args, **kwargs):
	        super(ProductReviewForm, self).__init__(*args, **kwargs) 		
	        if self.instance:
			self.fields['Store'].queryset = Store.objects.all()
			self.fields['Store'].empty_label = "-- Select a Store --"
	class Meta:
		model = ProductReview

		widgets = {'rating': forms.RadioSelect(attrs={'class':'star'}, renderer=StarsRadioFieldRenderer,   choices=RATING_CHOICES),}
		exclude = ('user','product', 'is_approved','slug',)


	def clean_user(self):
		user = self.cleaned_data['user']
		rev_check = ProductReview.objects.filter(user = request.user)
		if rev_check:
			raise forms.ValidationError('You Have Already Reviewed This Product')
		return self.cleaned_data['user']

class ProductForm(ModelForm):
	def __init__(self, *args, **kwargs):
	        super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['product_name'].error_messages['required'] = 'Please choose a Product Name'
		self.fields['product_image'].error_messages['required'] = 'Please choose a Product Image'
#		self.fields['product_thumbnail'].error_messages['required'] = 'Choose a Thumbnail or previous image'
		self.fields['brand'].error_messages['required'] = 'Please choose the Product Brand'
		self.fields['manufacturer'].error_messages['required'] = 'Please choose the Manufacturer of your product'
		self.fields['price'].error_messages['required'] = 'The price is required'
		self.fields['description'].error_messages['required'] = 'The description of your product is required'
		self.fields['Category'].error_messages['required'] = 'Choose the product Category(ies)'
		self.fields['product_type'].error_messages['required'] = 'Choose the product type'
		self.fields['product_pricing'].error_messages['required'] = 'Select a Pricing Option'
		self.fields['product_condition'].error_messages['required'] = 'Choose the Product Condition'
		self.fields['Store'].error_messages['required'] = 'Choose the product Store(s)'
		self.fields['quantity'].error_messages['required'] = 'Enter the Quantity'
		self.fields['quantity'].error_messages['invalid'] = 'Enter a valid Quantity value'
#		self.fields['recaptcha'].error_messages['required'] = 'Captcha Field is required'
#		self.fields["Store"].widget = forms.TextArea()

        	if self.instance:
			self.fields['Store'].queryset = Store.objects.all()
			self.fields['Store'].empty_label = "-- Select a Store --"

#	recaptcha = marcofucci_fields.ReCaptchaField()
#	, 'Store': SelectWithPopUp(), 

	Store = forms.ModelChoiceField(Store.objects.all(),widget=SelectWithPopUp)
	Category = forms.ModelMultipleChoiceField(Category.objects.all(), widget=MultipleSelectWithPopUp)
	product_type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect(renderer=HorizRadioRenderer))
	product_condition = forms.ChoiceField(choices=CONDITION_CHOICES, widget=forms.RadioSelect(renderer=HorizRadioRenderer))
	product_pricing = forms.ChoiceField(choices=PRICING_CHOICES, widget=forms.RadioSelect(renderer=HorizRadioRenderer))
#	product_category = forms.ModelChoiceField(Store.objects)

	class Meta:
		model = Product
		exclude = ('user','is_bestseller','is_featured','slug','is_active',)
#		Store = forms.ModelChoiceField(Store.objects, widget=SelectWithPopUp)

#My Custom validation Rules
	def clean_price(self):
		if self.cleaned_data['price'] <= 0:
			raise forms.ValidationError('Price must be greater than zero.')
		return self.cleaned_data['price']

class TransactionForm(ModelForm):

	def __init__(self, *args, **kwargs):
	        super(TransactionForm, self).__init__(*args, **kwargs)
		self.fields['bid_price'].error_messages['required'] = 'Please Fill in Bid Price'
		#self.fields['details'].error_messages['required'] = 'Send the product owner details about your Bid'
		self.fields['bid_price'].error_messages['invalid'] = 'The Bid Price is a figure'
		self.fields['quantity'].error_messages['required'] = 'Enter a value for the quantity'
		self.fields['quantity'].error_messages['invalid'] = 'Enter a Valid Quantity to Buy'


	class Meta:
		model = Transaction
		exclude = ('user','product','status')

	def clean_bid_price(self):
		''' offers = Transaction.objects.filter(product__slug=product_slug).order_by('-bid_price')[:1] '''
		if self.cleaned_data['bid_price'] <= 0:
			raise forms.ValidationError('Price must be greater than zero.')
		''' if self.cleaned_data['bid_price'] <= offers:
			raise forms.ValidationError('Price must be greater than Highest Bidder Offer.') '''
		return self.cleaned_data['bid_price']

	def clean_quantity(self):
#		p = get_object_or_404(Product, slug=product_slug)
#		if self.cleaned_data['quantity'] > p.quantity:
#			raise forms.ValidationError('%s is only available. Request for it or less' % (p.quantity))
		if self.cleaned_data['quantity'] <= 0:
			raise forms.ValidationError('Quantity must be greater than zero.')
		return self.cleaned_data['quantity']

class BuyNowForm(ModelForm):

	def __init__(self, *args, **kwargs):
	        super(BuyNowForm, self).__init__(*args, **kwargs)
		self.fields['quantity'].error_messages['required'] = 'Enter a value for the quantity'
		self.fields['quantity'].error_messages['invalid'] = 'Enter a Valid Quantity to Buy'


	class Meta:
		model = Buys
		exclude = ('user','product','status','price')

	def clean_quantity(self):
#		p = get_object_or_404(Product, slug=product_slug)
#		if self.cleaned_data['quantity'] > p.quantity:
#			raise forms.ValidationError('%s is only available. Request for it or less' % (p.quantity))
		if self.cleaned_data['quantity'] <= 0:
			raise forms.ValidationError('Quantity must be greater than zero.')
		return self.cleaned_data['quantity']

class ReplyForm(ModelForm):

	class Meta:
		model = Review_Reply
		widgets = {'rate_objective': forms.RadioSelect(attrs={'class':'star'}, renderer=StarsRadioFieldRenderer,   choices=USER_RATING_CHOICES), 'rate_complete': forms.RadioSelect(attrs={'class':'star'}, renderer=StarsRadioFieldRenderer,   choices=USER_RATING_CHOICES), }
		exclude = ('user','product', 'is_approved','review')


class TransactionReplyForm(ModelForm):

	def __init__(self, *args, **kwargs):
	        super(TransactionReplyForm, self).__init__(*args, **kwargs)
		self.fields['status'].error_messages['required'] = 'Accept or Reject this Buyer Offer'
		self.fields['quantity'].error_messages['required'] = 'Enter Quantity You can Offer the Buyer'
		self.fields['quantity'].error_messages['invalid'] = 'Enter a valid Quantity You can Offer the Buyer'

	status = forms.ChoiceField(choices=REPLY_CHOICES)

	class Meta:
		model = Transaction
		exclude = ('user','product', 'bid_price')

	def clean_quantity(self):
		if self.cleaned_data['quantity'] <= 0:
			raise forms.ValidationError('Quantity must be greater than zero.')
		return self.cleaned_data['quantity']


class BuyReplyForm(ModelForm):

	def __init__(self, *args, **kwargs):
	        super(BuyReplyForm, self).__init__(*args, **kwargs)
		self.fields['status'].error_messages['required'] = 'Accept or Reject this Buyer Offer'
		self.fields['quantity'].error_messages['required'] = 'Enter Quantity You can Offer the Buyer'
		self.fields['quantity'].error_messages['invalid'] = 'Enter a valid Quantity You can Offer the Buyer'

	status = forms.ChoiceField(choices=REPLY_CHOICES)

	class Meta:
		model = Buys
		exclude = ('user','product', 'price')

	def clean_quantity(self):
		if self.cleaned_data['quantity'] <= 0:
			raise forms.ValidationError('Quantity must be greater than zero.')
		return self.cleaned_data['quantity']

class FeedbackForm(ModelForm):

	def __init__(self, *args, **kwargs):
	        super(FeedbackForm, self).__init__(*args, **kwargs)
		self.fields['comment'].error_messages['required'] = 'Enter a small comment about this user'
		self.fields['rating'].error_messages['required'] = 'Choose a Rating for this user'

	class Meta:
		model = Feedback
		widgets = {'rating': forms.RadioSelect(attrs={'class':'star'}, renderer=StarsRadioFieldRenderer,   choices=USER_RATING_CHOICES),}
		exclude = ('user','product')

class ProductAddToCartForm(forms.Form):
    """ form class to add items to the shopping cart """
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity'}), 
                                  error_messages={'invalid':'Please enter a valid quantity.'}, 
                                  min_value=1)
    product_slug = forms.CharField(widget=forms.HiddenInput())
    
    def __init__(self, request=None, *args, **kwargs):
        """ override the default so we can set the request """
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)
    
    def clean(self):
        """ custom validation to check for presence of cookies in customer's browser """
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be enabled.")
        return self.cleaned_data

class PhotoForm(ModelForm):

	class Meta:
		model = Photo


