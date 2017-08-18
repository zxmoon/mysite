#!/usr/bin/env python
# -*- coding:utf8 -*-
# Title: 
# Author: xiang.zhang
# Date: 2017/8/16
# Description: 

from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^webtest/', views.webtest, name='webtest'),
	url(r'^Inetest/', views.Inetest, name='Inetest'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]











