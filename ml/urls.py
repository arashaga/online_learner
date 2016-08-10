# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('ml.views',
    url(r'^$', 'home', name='home'),
    url(r'^(?P<file_id>[0-9]+)$', 'train_using_regression', name='train_using_regression'),
)