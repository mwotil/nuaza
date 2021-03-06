from django.contrib import admin
from Nuaza.pdcts.models import Product, Category, ProductReview, Store, StoreReview, SuperCategory, Transaction, Buys
from forms import ProductForm


class ProductAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'price', 'submitted_at','is_active',)
	list_display_links = ('product_name',)
	list_per_page = 20
	ordering = ['-submitted_at']
	search_fields = ['product_name', 'description']
	prepopulated_fields = {'slug' : ('product_name',)}
admin.site.register(Product, ProductAdmin)

class SuperCategoryAdmin(admin.ModelAdmin):
	list_display = ('supercategory_name', 'created_at',)
	list_display_links = ('supercategory_name',)
	list_per_page = 10
	ordering = ['supercategory_name']
	search_fields = ['supercategory_name', ]
	prepopulated_fields = {'slug' : ('supercategory_name',)}
admin.site.register(SuperCategory, SuperCategoryAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name', 'created_at',)
	list_display_links = ('category_name',)
	list_per_page = 10
	ordering = ['category_name']
	search_fields = ['category_name', 'description']
	prepopulated_fields = {'slug' : ('category_name',)}
admin.site.register(Category, CategoryAdmin)

class ProductReviewAdmin(admin.ModelAdmin):
	list_display = ('product', 'user', 'title', 'date', 'rating', 'is_approved')
	list_per_page = 20
	list_filter = ('product', 'user', 'is_approved')
	ordering = ['date']
	search_fields = ['user','content','title']
admin.site.register(ProductReview, ProductReviewAdmin)

class StoreReviewAdmin(admin.ModelAdmin):
	list_display = ('store',)
	list_per_page = 20
	list_filter = ('store',)
	ordering = ['store']
	search_fields = ['store',]
admin.site.register(StoreReview, StoreReviewAdmin)

class StoreAdmin(admin.ModelAdmin):
	list_display = ('store_name','description','contacts',)
	list_per_page = 10
	list_filter = ('store_name',)
	ordering = ['store_name']
	search_fields = ['store_name',]
admin.site.register(Store, StoreAdmin)


class TransactionAdmin(admin.ModelAdmin):
	list_display = ('date', 'product', 'user', 'bid_price', 'status', 'quantity',)
	list_per_page = 20
	list_filter = ('date',)
	ordering = ['status']
	search_fields = ['product','status']
admin.site.register(Transaction, TransactionAdmin)

class BuysAdmin(admin.ModelAdmin):
	list_display = ('date', 'product', 'user', 'status', 'quantity', 'price')
	list_per_page = 20
	list_filter = ('date',)
	ordering = ['status']
	search_fields = ['product','status',]
admin.site.register(Buys, BuysAdmin)
