from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('entry_system.views',
    url(r'^$', 'entry'),
    url(r'^process/', 'process'),
    url(r'^drawing/', 'drawing'),
    url(r'^pick_winner/', 'pick_winner'),
    url(r'^winner/(?P<entry_id>\d+)', 'winner'),
)
