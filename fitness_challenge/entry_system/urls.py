from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('entry_system.views',
    url(r'^$', 'fitness_challenge'),
    url(r'^entry/', 'entry'),
    url(r'^process/', 'process'),
    url(r'^winner/', 'winner'),
)
