from django import template
from home.models import *

register = template.Library()

@register.filter
def getChild(parentID):
    return Category.objects.filter(cate_parent_id = parentID)

@register.filter
def hasChild(parentID):
    child = Category.objects.filter(cate_parent_id = parentID)
    if (child is not None):
        if len(child) > 0:
            return True
    return False
