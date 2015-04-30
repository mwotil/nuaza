from django.contrib import admin
from Nuaza.checkout.models import Order, OrderItem

class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','date','status','transaction_id','user')
    list_filter = ('status','date')
    search_fields = ('email','shipping_name','billing_name','id','transaction_id')
    inlines = [OrderItemInline,]
    
    fieldsets = (
                 ('Basics', {'fields': ('status','email','phone')}),
                 ('Shipping', {'fields':('shipping_name','shipping_address_1',
                'shipping_address_2','shipping_district','shipping_location')}),
                ('Billing', {'fields':('billing_name','billing_address_1',
                'billing_address_2','billing_district','billing_location')})
                 )
admin.site.register(Order, OrderAdmin)