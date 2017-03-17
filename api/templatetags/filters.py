# -*- coding: utf-8 -*-

from django import template
from api.utils import *

register = template.Library()

@register.filter(name='addLink')
def addLink(type):
    return getAddLink(type)
