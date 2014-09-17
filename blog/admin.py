# -*- coding: utf-8 -*-

from django.contrib import admin
from blog.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'creation_date', 'modification_date')
	search_field = ('name')
	date_hierarchy = 'creation_date'
	save_on_top = True
	prepopulated_fields = {'slug': ('name',)}
	
class EntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'status', 'author')
	search_fields = ('title', 'body')
	date_hierarchy = 'publication_date'
	fieldsets = (
		('Headline', {'fields': ('author', 'title', 'slug', 'category')}),
		('Publication', {'fields': ('publication_date', 'status')}),
		('Body', {'fields': ['pict', 'overview', 'body'], 'classes': ['tinymce']}),
	)
	save_on_top = True
	radio_fields = {'status': admin.VERTICAL}
	prepopulated_fields = {'slug': ('title',)}

	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)
