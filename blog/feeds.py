# -*- coding: utf-8 -*-
from django.utils.feedgenerator import Rss201rev2Feed
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from tagging.models import Tag, TaggedItem

from blog.models import Entry

class RssEntry(Feed):
	feed_type = Rss201rev2Feed
	title_template = "blog/feeds/entry_title.html"
	description_template = "blog/feeds/entry_description.html"

	def title(self):
		return _('Les derniers articles sur valentinbourgoin.net')

	def description(self):
		return _('Ingenieur multimedia freelance : developpement web, hebergement, conseil.')

	def link(self):
		return reverse('blog_index')

	def items(self):
		return Entry.online_objects.order_by('-publication_date')[:20]

	def item_pubdate(self, item):
		return item.publication_date

class RssCategory(RssEntry):
	def title(self, obj):
		return _('valentinbourgoin.net | Derniers articles "%s"') % obj

	def description(self, obj):
		site = Site.objects.get_current()
		return _('Derniers articles traitant de "%s" sur valentinbourgoin.net.') % obj

	def link(self, obj):
		return reverse('blog_index')

	def get_object(self, request, slug):
		return Tag.objects.get(name=slug)

	def items(self, obj):
                return TaggedItem.objects.get_by_model(Entry, obj).filter(status=Entry.STATUS_ONLINE).order_by('-publication_date')[:20]

	def item_pubdate(self, item):
		return item.publication_date