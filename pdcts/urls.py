from django.conf.urls.defaults import *


urlpatterns = patterns('Nuaza.pdcts.views',
  (r'^$', 'index', { 'template_name':'index.html'}, 'pdcts_home'),
  (r'^home/$', 'home', { 'template_name':'pdcts/index.html'}, 'pdcts_home'),  


  (r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', {'template_name':'pdcts/category.html'},'pdcts_category'),
  (r'^product/(?P<product_slug>[-\w]+)/$','show_product', {'template_name':'pdcts/product.html'},'pdcts_product'),
  (r'^store/(?P<store_slug>[-\w]+)/$','show_store', {'template_name':'pdcts/store.html'},'pdcts_store'),
  (r'^review/(?P<review_slug>[-\w]+)/$','show_review', {'template_name':'pdcts/review_details.html'},'pdcts_review'),
  (r'^review/product/add/$', 'add_review'),
  (r'^reply/review/add/$', 'add_reply'),
  (r'^shop/$','show_shop', {'template_name':'pdcts/shop.html'}, ),

  (r'^transact/(?P<product_slug>[-\w]+)/$', 'transact', {'template_name': 'pdcts/transact.html'}, 'transact'),
  (r'^buy-now/(?P<product_slug>[-\w]+)/$', 'buy_now', {'template_name': 'pdcts/buy-now.html'}, 'buy_now'),

  (r'^rate_user/(?P<product_slug>[-\w]+)/$', 'rate_user', {'template_name': 'pdcts/rate_user.html'}, 'rate_user'),

  (r'^reply_transact/(?P<transaction_id>[-\w]+)/$', 'reply_transact', {'template_name': 'pdcts/reply_transact.html'}, 'reply_transact'),
  (r'^reply_buy/(?P<buy_id>[-\w]+)/$', 'reply_buy', {'template_name': 'pdcts/reply_buy.html'}, 'reply_buy'),


  (r'^shops_all/$','show_all_shops', {'template_name':'pdcts/shops_all.html'}, ),

 (r'^Buy-a-Product/$','product_listing', {'template_name':'pdcts/pdct_listing.html'}, ),

  (r'^product_info/(?P<product_slug>[-\w]+)/$', 'product_info', {'template_name': 'pdcts/poduct_edit.html'}, 'product_info'),
  (r'^review_info/(?P<review_slug>[-\w]+)/$', 'review_info', {'template_name': 'pdcts/review_edit.html'}, 'review_info'),
  (r'^add_product/$', 'add_product', {'template_name':'pdcts/add.html'}, 'add_product'),
   
  (r'^photos/upload/$', 'upload_photo'),

)
