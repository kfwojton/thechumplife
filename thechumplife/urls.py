from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *
from django import forms
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from re import *
import os
import django

admin_media_url = settings.ADMIN_MEDIA_PREFIX.lstrip('/') + '(?P<path>.*)$'
admin_media_path = os.path.join(django.__path__[0], 'contrib', 'admin', 'media')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hub3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/(.*)', article),
    url(r'^a/(.*)',auto),

    url(r'^$', start),



    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^' + admin_media_url , 'django.views.static.serve', {'document_root': admin_media_path,}, name='admin-media'),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns += staticfiles_urlpatterns()
