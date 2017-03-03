from django.conf.urls import url
from django.contrib import admin

# from django.contrib.flatpages import views

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	url(r'^$', post_list, name='list'),
	# url(r'^/pages/contact/$', contact, name='contact'),
	# url(r'^/pages/about-me/$', about-me, name='about-me'),

    url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
