from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

###
# Homepage
###
def index(request):
	# Get KM cycled from Strava API 
	from stravalib.client import Client 
	from stravalib import unithelper
	strava = Client(settings.STRAVA_TOKEN)
	profile = strava.get_athlete(settings.STRAVA_ID)
	cycled = 0
	for b in profile.bikes: 
		cycled += float(b.distance) / 1000

	return render_to_response(
		'cv/index.html', 
		locals(),
		context_instance=RequestContext(request)
	)

###
# CV
###
def cv(request):
	return render_to_response(
		'cv/cv.html', 
		locals(),
		context_instance=RequestContext(request)
	)

###
# Contact
###
def contact(request):
	return render_to_response(
		'cv/contact.html', 
		locals(),
		context_instance=RequestContext(request)
	)