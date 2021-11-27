from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag
def title(Data="Blog"):
    return Data

@register.inclusion_tag('blog/categro_navbar.html')
def category_navbar():
    categories = Category.objects.activ_cat()
    return {'category_list': categories}

@register.inclusion_tag('registration/partials/link.html')
def link(request, link_name, content, link_icon):
    return {'request': request, 
            'link_name': link_name,
            'content': content,
            'link_icon': link_icon,
            'link': "accounts:{}".format(link_name),
            }