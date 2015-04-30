# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reputation_Check'
        db.create_table('reputation_check', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reputation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pdcts.User_Reputation'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('pdcts', ['Reputation_Check'])

    def backwards(self, orm):
        # Deleting model 'Reputation_Check'
        db.delete_table('reputation_check')

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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        'pdcts.reputation_check': {
            'Meta': {'object_name': 'Reputation_Check', 'db_table': "'reputation_check'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reputation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pdcts.User_Reputation']"}),
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