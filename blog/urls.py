from django.conf.urls import re_path
from blog.views import *

app_name = 'blog'


urlpatterns = [
    # simple blog post
    re_path('^$', BlogHomeView.as_view(), name='home_blog'),
    re_path(r'^(?P<slug>[-\w]+)-(?P<pk>\d+)/$', BlogDetailView.as_view(), name='blog_details'),
    # question post
    re_path('question/', QuestionPostView.as_view(), name='question_list'),
    re_path('(?P<slug>[-\w]+)/$', QuestionDetailView.as_view(), name='question__details'),
]


