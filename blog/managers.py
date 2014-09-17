from django.db import models

class CategoryOnlineManager(models.Manager):

	def get_queryset(self):
		from blog.models import Entry
		entry_status = Entry.STATUS_ONLINE
		return super(CategoryOnlineManager, self).get_queryset().filter(
			entry__status=entry_status).distinct()

class EntryOnlineManager(models.Manager):

	def get_queryset(self):
		return super(EntryOnlineManager, self).get_queryset().filter(
			status=self.model.STATUS_ONLINE)