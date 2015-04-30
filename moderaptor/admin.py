#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin
from moderaptor.models import ModReport, AbuseType, Banzor, CensoredWord

class ModReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'object', 'user', 'type', 'date_added', 'resolved', 'date_resolved', 'hide_object',)
    list_filter = ('resolved', 'hide_object',)
    list_per_page = 30
    search_fields = ['id', 'title', 'user__last_name', 'user__first_name', 'user__username']
    raw_id_fields = ('user',)

admin.site.register(ModReport, ModReportAdmin)

class AbuseTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'ordering', 'rank',)
    list_per_page = 30
    search_fields = ['id', 'title', 'description',]
    
admin.site.register(AbuseType, AbuseTypeAdmin)

class BanzorAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_added', 'active',)
    list_per_page = 30
    search_fields = ['user',]
    
admin.site.register(Banzor, BanzorAdmin)

class CensoredAdmin(admin.ModelAdmin):
    list_display = ('word',)
    
admin.site.register(CensoredWord, CensoredAdmin)