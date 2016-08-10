from django.conf.urls import patterns, include, url
from django.contrib import admin
# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'ml.views.list', name='list'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('ml.urls')),
)
