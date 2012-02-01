from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('entry_system.views',
    url(r'^$', 'entry'),
    url(r'^process/', 'process'),
)
