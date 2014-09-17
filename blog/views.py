# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from blog.models import Entry


###
# Blog index 
# Lists all online posts 
###
def blog_index(request):
	# Get paged objects
	objects = Entry.online_objects.order_by('-publication_date')
	paginator = Paginator(objects, 6)
	page = int(request.GET.get('page', '1'))
	try:
		entries = paginator.page(page)
	except (EmptyPage, InvalidPage):
		entries = paginator.page(paginator.num_pages)
	
	# Render template 
	return render_to_response(
		'blog/list.html', 
		{ 'entries': entries }, 
		context_instance=RequestContext(request)
	)



def blog_detail(request, slug):
	entry = get_object_or_404(Entry, slug=slug)
	previous = entry.get_previous_entry()
	next = entry.get_next_entry()
	return render_to_response(
		'blog/detail.html', 
		{
			'entry': entry, 
			'previous': previous, 
			'next': next
		}, 
		context_instance=RequestContext(request))
	
	