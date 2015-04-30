#!/usr/bin/env python
# encoding: utf-8

import os
from django import forms
from django.db import models
from django.db.models import Q
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from django.db.models.loading import get_model

import moderaptor
import moderaptor.settings as mod_settings
from moderaptor.models import ModReport, AbuseType
from moderaptor.utils import is_moderator
from django.shortcuts import get_object_or_404


class WtfBlogPost(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['id']

try:
    moderaptor.register(WtfBlogPost)
except moderaptor.AlreadyRegistered:
    pass    
   
   
class TestModerator(TestCase):
    def setUp(self):
        self.client = Client()
        user,created = User.objects.get_or_create(username='test')
        user.set_password('test')
        user.save()
        self.user = user
        
    def test_not_moderator(self):
        self.assertEqual(is_moderator(self.user), False)
        
    def test_moderator(self):
        for id in mod_settings.MODERATORS_GROUPS_IDS:
            group,created = Group.objects.get_or_create(id=id, name="grupen")
            self.user.groups.add(group)
        self.assertEqual(is_moderator(self.user), True)    


class TestReport(TestCase):
    def setUp(self):
        self.client = Client()
        user,created = User.objects.get_or_create(username='test')
        user.set_password('test')
        user.save()
        self.user = user
        self.post = WtfBlogPost.objects.create(id=1, title='lolzorin', text='whyhellothere')
    
    def log_in(self):
        login = self.client.login(username='test', password='test')
        self.failUnless(login, 'Could not log in')
               
    def test_view(self):
        response = self.client.get('/moderaptor/report/moderaptor/wtfblogpost/1/')
        self.assertRedirects(response, '/accounts/login/?next=/moderaptor/report/moderaptor/wtfblogpost/1/')
        
        self.log_in()
        
        response = self.client.get('/moderaptor/report/moderaptor/wtfblogpost/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"error": "No data"}')
        
    def test_post_view(self):
        post = {'type':1}
        
        if mod_settings.SIGNED_IN_ONLY:
            response = self.client.post('/moderaptor/report/moderaptor/wtfblogpost/1/', post)
            self.assertRedirects(response, '/accounts/login/?next=/moderaptor/report/moderaptor/wtfblogpost/1/')
            
            login = self.client.login(username='test', password='test')
            self.failUnless(login, 'Could not log in')
    
        response = self.client.post('/moderaptor/report/moderaptor/wtfblogpost/1111111/', post)
        self.assertEqual(response.status_code, 404)
        
        response = self.client.post('/moderaptor/report/moderaptor/wtfblogpost/1/', post)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"message": "reported", "id": 1}')
    
    def test_post_view_bad_type(self):
        post = {'type':112312}
        
        response = self.client.post('/moderaptor/report/moderaptor/wtfblogpost/1/', post)
        self.assertRedirects(response, '/accounts/login/?next=/moderaptor/report/moderaptor/wtfblogpost/1/')
        
        self.log_in()

        response = self.client.post('/moderaptor/report/moderaptor/wtfblogpost/1/', post)
        self.assertEqual(response.status_code, 404)
   
        
class TestQuickMod(TestCase):
    def setUp(self):
        self.client = Client()
        user,created = User.objects.get_or_create(username='test')
        user.set_password('test')
        user.save()
        self.user = user
        for id in mod_settings.MODERATORS_GROUPS_IDS:
            group,created = Group.objects.get_or_create(id=id, name="grupen")
            self.user.groups.add(group)
            
        self.post = WtfBlogPost.objects.create(title='lolzorin', text='whyhellothere')
        type = AbuseType.objects.get(id=1)   
        model = 'wtfblogpost'
        #ctype = ContentType.objects.get_by_natural_key('moderaptor', model)
        ctype = ContentType.objects.get(app_label='moderaptor', model=model)
        object = get_object_or_404(ctype, id=self.post.id)
        self.report = ModReport.objects.create(id=1, user=self.user, type=type, content_type=ctype, object_id=self.post.id, object=object, ip='127.0.0.1')         
    
    def log_in(self):
        login = self.client.login(username='test', password='test')
        self.failUnless(login, 'Could not log in')
        
    def test_action_submit(self):
        self.log_in()
        
        post = {'action': 'hide'}
        
        response = self.client.post('/moderaptor/moderate/1/', post)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"message": "moderated", "id": 1}')
    
    def test_action_bad_submit(self):
        self.log_in()
        
        post = {'action': 'yo'}
        
        response = self.client.post('/moderaptor/moderate/11111111/', post)
        self.assertEqual(response.status_code, 404)
        
        response = self.client.post('/moderaptor/moderate/1/', post)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '{"error": "No data"}')

