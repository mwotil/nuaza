# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'UserProfile.phone_number'
        db.delete_column('accounts_userprofile', 'phone_number')

        # Deleting field 'UserProfile.Address_1'
        db.delete_column('accounts_userprofile', 'Address_1')

        # Deleting field 'UserProfile.Address_2'
        db.delete_column('accounts_userprofile', 'Address_2')

        # Deleting field 'UserProfile.Email_Address'
        db.delete_column('accounts_userprofile', 'Email_Address')

        # Adding field 'UserProfile.email'
        db.add_column('accounts_userprofile', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='xyz@example.com', max_length=50),
                      keep_default=False)

        # Adding field 'UserProfile.phone'
        db.add_column('accounts_userprofile', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='My Phone Number', max_length=20),
                      keep_default=False)

        # Adding field 'UserProfile.shipping_name'
        db.add_column('accounts_userprofile', 'shipping_name',
                      self.gf('django.db.models.fields.CharField')(default='My Shipping Name', max_length=50),
                      keep_default=False)

        # Adding field 'UserProfile.shipping_address_1'
        db.add_column('accounts_userprofile', 'shipping_address_1',
                      self.gf('django.db.models.fields.CharField')(default='My Shipping Address', max_length=50),
                      keep_default=False)

        # Adding field 'UserProfile.shipping_address_2'
        db.add_column('accounts_userprofile', 'shipping_address_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.shipping_district'
        db.add_column('accounts_userprofile', 'shipping_district',
                      self.gf('django.db.models.fields.CharField')(default='My Shipping District', max_length=50),
                      keep_default=False)

        # Adding field 'UserProfile.shipping_location'
        db.add_column('accounts_userprofile', 'shipping_location',
                      self.gf('django.db.models.fields.CharField')(default='My Shipping Location', max_length=50),
                      keep_default=False)

        # Adding field 'UserProfile.billing_name'
        db.add_column('accounts_userprofile', 'billing_name',
                      self.gf('django.db.models.fields.CharField')(default='My Billing Name', max_length=50),
                      keep_default=False)

        # Adding field 'UserProfile.billing_address_1'
        db.add_column('accounts_userprofile', 'billing_address_1',
                      self.gf('django.db.models.fields.CharField')(default='My Billing Address', max_length=50),
                      keep_default=False)

        # Adding field 'UserProfile.billing_address_2'
        db.add_column('accounts_userprofile', 'billing_address_2',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.billing_district'
        db.add_column('accounts_userprofile', 'billing_district',
                      self.gf('django.db.models.fields.CharField')(default='My Billing District', max_length=50),
                      keep_default=False)

        # Adding field 'UserProfile.billing_location'
        db.add_column('accounts_userprofile', 'billing_location',
                      self.gf('django.db.models.fields.CharField')(default='My Billing Location', max_length=50),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'UserProfile.phone_number'
        db.add_column('accounts_userprofile', 'phone_number',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.Address_1'
        db.add_column('accounts_userprofile', 'Address_1',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2012, 8, 26, 0, 0), max_length=25),
                      keep_default=False)

        # Adding field 'UserProfile.Address_2'
        db.add_column('accounts_userprofile', 'Address_2',
                      self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.Email_Address'
        db.add_column('accounts_userprofile', 'Email_Address',
                      self.gf('django.db.models.fields.EmailField')(default=datetime.datetime(2012, 8, 26, 0, 0), max_length=75),
                      keep_default=False)

        # Deleting field 'UserProfile.email'
        db.delete_column('accounts_userprofile', 'email')

        # Deleting field 'UserProfile.phone'
        db.delete_column('accounts_userprofile', 'phone')

        # Deleting field 'UserProfile.shipping_name'
        db.delete_column('accounts_userprofile', 'shipping_name')

        # Deleting field 'UserProfile.shipping_address_1'
        db.delete_column('accounts_userprofile', 'shipping_address_1')

        # Deleting field 'UserProfile.shipping_address_2'
        db.delete_column('accounts_userprofile', 'shipping_address_2')

        # Deleting field 'UserProfile.shipping_district'
        db.delete_column('accounts_userprofile', 'shipping_district')

        # Deleting field 'UserProfile.shipping_location'
        db.delete_column('accounts_userprofile', 'shipping_location')

        # Deleting field 'UserProfile.billing_name'
        db.delete_column('accounts_userprofile', 'billing_name')

        # Deleting field 'UserProfile.billing_address_1'
        db.delete_column('accounts_userprofile', 'billing_address_1')

        # Deleting field 'UserProfile.billing_address_2'
        db.delete_column('accounts_userprofile', 'billing_address_2')

        # Deleting field 'UserProfile.billing_district'
        db.delete_column('accounts_userprofile', 'billing_district')

        # Deleting field 'UserProfile.billing_location'
        db.delete_column('accounts_userprofile', 'billing_location')

    models = {
        'accounts.userprofile': {
            'First_Name': ('django.db.models.fields.CharField', [], {'default': "'My First Name'", 'max_length': '25'}),
            'Last_Name': ('django.db.models.fields.CharField', [], {'default': "'My Last Name'", 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'UserProfile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'billing_address_1': ('django.db.models.fields.CharField', [], {'default': "'My Billing Address'", 'max_length': '50'}),
            'billing_address_2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'billing_district': ('django.db.models.fields.CharField', [], {'default': "'My Billing District'", 'max_length': '50'}),
            'billing_location': ('django.db.models.fields.CharField', [], {'default': "'My Billing Location'", 'max_length': '50'}),
            'billing_name': ('django.db.models.fields.CharField', [], {'default': "'My Billing Name'", 'max_length': '50'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "'xyz@example.com'", 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': "'My Phone Number'", 'max_length': '20'}),
            'shipping_address_1': ('django.db.models.fields.CharField', [], {'default': "'My Shipping Address'", 'max_length': '50'}),
            'shipping_address_2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'shipping_district': ('django.db.models.fields.CharField', [], {'default': "'My Shipping District'", 'max_length': '50'}),
            'shipping_location': ('django.db.models.fields.CharField', [], {'default': "'My Shipping Location'", 'max_length': '50'}),
            'shipping_name': ('django.db.models.fields.CharField', [], {'default': "'My Shipping Name'", 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'userImg': ('stdimage.fields.StdImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
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
        }
    }

    complete_apps = ['accounts']