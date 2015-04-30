from django.contrib import admin
from models import Request
from forms import RequestForm


class RequestAdmin(admin.ModelAdmin):
	list_display = ('product_name', 'price', 'submitted_at','is_active',)
	list_display_links = ('product_name',)
	list_per_page = 20
	ordering = ['-submitted_at']
	search_fields = ['product_name', 'description']
#	prepopulated_fields = {'slug' : ('product_name',)}
admin.site.register(Request, RequestAdmin)

