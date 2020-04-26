from post.models import Post
from django import template

register = template.Library()

@register.simple_tag  #we can pass name='my_name' as parameter for specific name
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('post/latest_posts.html')
def show_latest_posts(count=3):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}


#Assignment tag is deprecated It's valid till django 2.0

# from django.db.models import Count
# @register.assignment_tag
# def get_most_commented_posts(count=3):
#     return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

from django.db.models import Count
@register.inclusion_tag('post/most_commented_posts.html')
def get_most_commented_posts(count=3):
    most_commented = Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return {'most_commented':most_commented}
