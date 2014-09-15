from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'cv.views.index', name='index'),
    url(r'^cv/$', 'cv.views.cv', name='cv'),
)
