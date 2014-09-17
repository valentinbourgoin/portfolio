# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from blog.feeds import *
from blog.views import *


urlpatterns = patterns('',
	url(r'^feed/rss/$', RssEntry(), name='RssEntry'),
    url(r'^feed/rss/category/(?P<slug>[\w-]+)/$', RssCategory(), name='RssCategory'),

	url(r'^$', blog_index, name='blog_index'),
	url(r'^article/(?P<slug>[\w-]+)/$', blog_detail, name='blog_detail'),
	
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
