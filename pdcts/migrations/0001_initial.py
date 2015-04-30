# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SuperCategory'
        db.create_table('supercategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supercategory_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=())),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('pdcts', ['SuperCategory'])

        # Adding model 'Category'
        db.create_table('category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=())),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('supercategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.SuperCategory'])),
        ))
        db.send_create_signal('pdcts', ['Category'])

        # Adding model 'Store'
        db.create_table('store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store_name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=())),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('contacts', self.gf('django.db.models.fields.TextField')()),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('pdcts', ['Store'])

        # Adding model 'Product'
        db.create_table('product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=())),
            ('product_image', self.gf('stdimage.fields.StdImageField')(max_length=100, blank=True)),
            ('brand', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('Store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.Store'], null=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4)),
            ('submitted_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('product_type', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('product_condition', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('product_pricing', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_bestseller', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('pdcts', ['Product'])

        # Adding M2M table for field Category on 'Product'
        db.create_table('product_Category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm['pdcts.product'], null=False)),
            ('category', models.ForeignKey(orm['pdcts.category'], null=False))
        ))
        db.create_unique('product_Category', ['product_id', 'category_id'])

        # Adding model 'ProductReview'
        db.create_table('pdcts_productreview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.Product'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('Store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.Store'], null=True)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=())),
        ))
        db.send_create_signal('pdcts', ['ProductReview'])

        # Adding model 'StoreReview'
        db.create_table('pdcts_storereview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.Product'])),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.Store'])),
            ('rating_votes', self.gf('django.db.models.fields.PositiveIntegerField')(default=0, blank=True)),
            ('rating_score', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('pdcts', ['StoreReview'])

        # Adding model 'Review_Reply'
        db.create_table('pdcts_review_reply', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.ProductReview'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('reply', self.gf('django.db.models.fields.TextField')()),
            ('rate_objective', self.gf('django.db.models.fields.FloatField')()),
            ('rate_complete', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('pdcts', ['Review_Reply'])

        # Adding model 'User_Reputation'
        db.create_table('pdcts_user_reputation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('reputation', self.gf('django.db.models.fields.FloatField')()),
            ('entity_alpha', self.gf('django.db.models.fields.FloatField')()),
            ('entity_beta', self.gf('django.db.models.fields.FloatField')()),
            ('votes', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('pdcts', ['User_Reputation'])

        # Adding model 'Transaction'
        db.create_table('transaction', (
            ('transact_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.Product'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('bid_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4)),
        ))
        db.send_create_signal('pdcts', ['Transaction'])

        # Adding model 'Buys'
        db.create_table('buys', (
            ('buy_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.Product'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1, max_length=4)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('pdcts', ['Buys'])

        # Adding model 'Feedback'
        db.create_table('feedback', (
            ('feedback_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.Product'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('pdcts', ['Feedback'])

    def backwards(self, orm):
        # Deleting model 'SuperCategory'
        db.delete_table('supercategory')

        # Deleting model 'Category'
        db.delete_table('category')

        # Deleting model 'Store'
        db.delete_table('store')

        # Deleting model 'Product'
        db.delete_table('product')

        # Removing M2M table for field Category on 'Product'
        db.delete_table('product_Category')

        # Deleting model 'ProductReview'
        db.delete_table('pdcts_productreview')

        # Deleting model 'StoreReview'
        db.delete_table('pdcts_storereview')

        # Deleting model 'Review_Reply'
        db.delete_table('pdcts_review_reply')

        # Deleting model 'User_Reputation'
        db.delete_table('pdcts_user_reputation')

        # Deleting model 'Transaction'
        db.delete_table('transaction')

        # Deleting model 'Buys'
        db.delete_table('buys')

        # Deleting model 'Feedback'
        db.delete_table('feedback')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'pdcts.buys': {
            'Meta': {'ordering': "['-product']", 'object_name': 'Buys', 'db_table': "'buys'"},
            'buy_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '4'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'pdcts.category': {
            'Meta': {'ordering': "['-created_at']", 'object_name': 'Category', 'db_table': "'category'"},
            'category_name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'supercategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.SuperCategory']"})
        },
        'pdcts.feedback': {
            'Meta': {'ordering': "['-rating']", 'object_name': 'Feedback', 'db_table': "'feedback'"},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'feedback_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.Product']"}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'pdcts.product': {
            'Category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['pdcts.Category']", 'symmetrical': 'False'}),
            'Meta': {'ordering': "['-submitted_at']", 'object_name': 'Product', 'db_table': "'product'"},
            'Store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.Store']", 'null': 'True'}),
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_bestseller': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'product_condition': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'product_image': ('stdimage.fields.StdImageField', [], {'max_length': '100', 'blank': 'True'}),
            'product_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'product_pricing': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'product_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '4'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'submitted_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'pdcts.productreview': {
            'Meta': {'object_name': 'ProductReview'},
            'Store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.Store']", 'null': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.Product']"}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'pdcts.review_reply': {
            'Meta': {'object_name': 'Review_Reply'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rate_complete': ('django.db.models.fields.FloatField', [], {}),
            'rate_objective': ('django.db.models.fields.FloatField', [], {}),
            'reply': ('django.db.models.fields.TextField', [], {}),
            'review': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.ProductReview']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'pdcts.store': {
            'Meta': {'ordering': "['-store_name']", 'object_name': 'Store', 'db_table': "'store'"},
            'contacts': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'store_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'pdcts.storereview': {
            'Meta': {'object_name': 'StoreReview'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.Product']"}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.Store']"})
        },
        'pdcts.supercategory': {
            'Meta': {'ordering': "['supercategory_name']", 'object_name': 'SuperCategory', 'db_table': "'supercategory'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'}),
            'supercategory_name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'pdcts.transaction': {
            'Meta': {'ordering': "['-product']", 'object_name': 'Transaction', 'db_table': "'transaction'"},
            'bid_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '4'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'transact_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'pdcts.user_reputation': {
            'Meta': {'object_name': 'User_Reputation'},
            'entity_alpha': ('django.db.models.fields.FloatField', [], {}),
            'entity_beta': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reputation': ('django.db.models.fields.FloatField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'votes': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['pdcts']