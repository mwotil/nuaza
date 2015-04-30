#!/usr/bin/env python
# encoding: utf-8

from django import template
from moderaptor.models import CensoredWord

register = template.Library()

@register.filter(name='mod_censored')
def censored(text):
    """
    
    """
    for cw in CensoredWord.objects.all():
        word = cw.word
        uncovered = len(word)*2/5 if len(word)>4 else 3  
        text = text.replace(word, word[:uncovered]+'*'*(len(word)-uncovered))
    return text