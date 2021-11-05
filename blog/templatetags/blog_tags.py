from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag
def title(Data="Blog"):
    return Data

@register.inclusion_tag('blog/category_navbar.html')
def category_navbar():
    categories = Category.objects.all()
    return {'category_list': categories}