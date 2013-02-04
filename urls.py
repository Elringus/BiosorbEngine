from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    url(r'^$', 'website.views.index'),
    #url(r'^about/$', 'website.views.about'),
    url(r'^articles/(?P<article_id>.*)$', 'website.views.article'),
    #url(r'^contacts/$', 'website.views.contact'),

    url(r'^game/auth', 'game.views.auth'),
    url(r'^game/get_scorelist', 'game.views.get_scorelist'),
    url(r'^game/add_score', 'game.views.add_score'),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
)
