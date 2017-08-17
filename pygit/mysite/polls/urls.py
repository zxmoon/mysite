#!/usr/bin/env python
# -*- coding:utf8 -*-
# Title: 
# Author: xiang.zhang
# Date: 2017/8/16
# Description: 

from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^webtest/', views.webtest, name='webtest'),
	url(r'^Inetest/', views.Inetest, name='Inetest')
]











