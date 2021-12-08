from django import template
from blog.models import Article, Category

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

@register.inclusion_tag('blog/blog-side-categories.html')
def SidebarCategories():
    articles = Article.objects.published()
    categories = Category.objects.activ_cat()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = articles.filter(category=name).count()
    return {'categories': cat_dict}

@register.inclusion_tag('blog/blog-side-recentposts.html')
def SidebarRecentPosts():
    articles = Article.objects.published()[:5]
    return {'articles': articles}
    
    