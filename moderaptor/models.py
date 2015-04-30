#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _


class AbuseType(models.Model):
    """
    Type of abuse (f.ex. violation of terms, offensive lang, etc.)
    """
    title = models.CharField(_('title'), max_length=32)
    description = models.TextField(_('description'), null=True, blank=True)
    ordering = models.IntegerField(_('order on list'), null=True, blank=True)
    rank = models.IntegerField(_('abuse rank'), default=1)

    class Meta:
        ordering = ['ordering', 'title', 'id',]
        verbose_name = _('abuse type')
        verbose_name_plural = _('abuse types')
        
    def __unicode__(self):
        return self.title
    
  
class ModReportManager(models.Manager):
    def get_for_object(self, obj):
        ctype = ContentType.objects.get_for_model(obj)
        return self.filter(content_type__pk=ctype.pk,
                           object_id=obj.pk)
        
                     
class ModReport(models.Model):    
    """
    Report of the object (such as post, comment) which abuses your website        
    """
    user = models.ForeignKey(User, verbose_name=_('who reported'), related_name='snitch')
    type = models.ForeignKey(AbuseType, verbose_name=_('abuse type'))
    
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
    object_id = models.PositiveIntegerField(_('object id'), db_index=True)
    object = generic.GenericForeignKey('content_type', 'object_id')

    ip = models.IPAddressField(max_length=15)
    date_added = models.DateTimeField(_('when added'), default=datetime.now)
        
    resolved = models.BooleanField(_('mark as resolved'), default=False)
    date_resolved = models.DateTimeField(_('when resolved'), null=True, blank=True)
    who_resolved = models.ForeignKey(User, verbose_name=_('moderator'), related_name='moderator', null=True, blank=True)
    
    hide_object = models.BooleanField(_('hide element from public view'), default=False)
    admin_comment = models.TextField(_('admin comment'), null=True, blank=True)
        
    objects = ModReportManager()
    
    class Meta:
        ordering = ['-id',]
        unique_together = ['content_type', 'object_id'] 
        verbose_name = _('report')
        verbose_name_plural = _('reports')
        
    def __unicode__(self):
        return u"Mod report #%s" % str(self.id)
    


class CensoredWord(models.Model):    
    """
    Word that should be censored in text
    """
    word = models.CharField(_('word'), max_length=32)
    
    class Meta:
        ordering=['word',]
        verbose_name = _('censored word')
        verbose_name_plural = _('censored words')

    def __unicode__(self):
        return u"%s" % self.word
 
      
   
class Banzor(models.Model):
    """
    User bans. It deactivates the banned user when added/activated and activates him back when deleted/deactivated. 
    
    Note that it's completely independent from any permission management you implemented and doesn't override your auth in any way. 
    It just offers a simple way to save information about bans.
    """
    user = models.OneToOneField(User)
    date_added = models.DateTimeField(_('when added'), default=datetime.now)
    active = models.BooleanField(_('active ban?'), default=True)
    admin_comment = models.TextField(_('admin comment'), null=True, blank=True)
    
    class Meta:
        ordering = ['-id',]
        verbose_name = _('ban')
        verbose_name_plural = _('bans')
        
    def __unicode__(self):
        return u"Ban %s" % str(self.user.get_profile())
        
    def save(self, *args, **kwargs):
        super(Banzor, self).save(*args, **kwargs)
        user = User.objects.get(id=self.user.id)
        user.is_active = not self.active
        user.save()
    
    def delete(self, *args, **kwargs):
        user = User.objects.get(id=self.user.id)
        user.is_active = True
        user.save()
        super(Banzor, self).save(*args, **kwargs)
        
        