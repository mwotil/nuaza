from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from stdimage import StdImageField
from autoslug import AutoSlugField

class AndroidProduct(models.Model):
	product_name = models.CharField(max_length = 50)
	slug = AutoSlugField(unique=True, populate_from='product_name', editable=True) 
	brand = models.CharField(max_length = 25)
	manufacturer = models.CharField(max_length = 25)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, null=True, blank=True)
	quantity = models.IntegerField(max_length=4,default=1)
	submitted_at = models.DateTimeField(auto_now_add=True)
	description = models.TextField()
	is_active = models.BooleanField(default=False)
    	is_bestseller = models.BooleanField(default=False)
    	is_featured = models.BooleanField(default=False)
	user = models.ForeignKey(User)
 
 	def __unicode__ (self):
		return self.product_name

	class Meta:
		db_table ='androidproduct'
		ordering = ['-submitted_at']
		verbose_name_plural = 'Products'
    
#admin.site.register(AndroidProduct)

class Photo(models.Model):
        title = models.CharField(max_length=255,blank=True)
        photo = StdImageField(upload_to='images/products/main', blank=True, size=(350, 400), thumbnail_size=(100, 100, True)) 
        description = models.TextField(blank=True)
        uploaded = models.DateTimeField(auto_now_add=True)
        modified = models.DateTimeField(auto_now=True)
        class Meta:
            db_table = 'Android_photos'
        def __unicode__(self):
            return '%s' % self.title