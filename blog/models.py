# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from tagging.fields import *
from tagging.models import Tag
from django.utils.translation import ugettext_lazy as _
from blog.managers import CategoryOnlineManager
from blog.managers import EntryOnlineManager


class Category(models.Model):
	name = models.CharField(_('name'), max_length=255)
	slug = models.SlugField(_('slug'), max_length=255, unique=True)
	class_name = models.CharField(_('class name'), max_length=255, blank=True, null=True)
	creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
	modification_date = models.DateTimeField(_('modification date'), auto_now=True) 
	objects = models.Manager()
	online_objects = CategoryOnlineManager()

	class Meta:
		verbose_name = _('category')
		verbose_name_plural = _('categories')

	def __unicode__(self):
		return u'%s' % self.name

	@models.permalink
	def get_absolute_url(self):
		return ('blog_category', (), {
			'slug': self.slug,
		})
		
	def _get_online_entries(self):
		from blog.models import Entry
		return self.entry_set.filter(status=Entry.STATUS_ONLINE)
	
	online_entry_set = property(_get_online_entries)
	


class Entry(models.Model):
	STATUS_OFFLINE = 0
	STATUS_ONLINE = 1
	STATUS_DEFAULT = STATUS_OFFLINE
	STATUS_CHOICES = (
		(STATUS_OFFLINE, _('Offline')),
		(STATUS_ONLINE, _('Online')),
	)

	title = models.CharField(_('title'), max_length=255)
	slug = models.SlugField(_('slug'), max_length=255, unique_for_date='publication_date')
	author = models.ForeignKey('auth.User', verbose_name=_('author'))
	pict = models.ImageField(upload_to='img/entries/', blank=True, null=True)
	category = models.ForeignKey(Category, verbose_name=_('category'))
	publication_date = models.DateTimeField(_('publication date'), default=datetime.now(), db_index=True)
	status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_DEFAULT, db_index=True)
	body = models.TextField(_('body'))
	tags = models.TextField(null=True)
	overview = models.TextField()
	
	objects = models.Manager()
	online_objects = EntryOnlineManager()

	class Meta:
		verbose_name = _('article')
		verbose_name_plural = _('articles')

	def __unicode__(self):
		return u'%s' % self.title

	@models.permalink
	def get_absolute_url(self):
		return ('blog_detail', (), {
			'slug': self.slug,
		})
	
	def get_next_entry(self):
		q = Entry.online_objects.filter(publication_date__gte=self.publication_date).exclude(id=self.id).order_by('publication_date')[:1]
		if q.count() > 0:
			return q.get()
	
	def get_previous_entry(self):
		q = Entry.online_objects.filter(publication_date__lte=self.publication_date).exclude(id=self.id).order_by('-publication_date')[:1]
		if q.count() > 0:
			return q.get()