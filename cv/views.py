from django.shortcuts import render
from django.shortcuts import render_to_response

# Homepage
def index(self):
	return render_to_response('cv/index.html', {})

# CV
def cv(self):
	return render_to_response('cv/cv.html', {})

# Contact
def contact(self):
	return render_to_response('cv/contact.html', {})