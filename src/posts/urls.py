from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	post_content,
	post_update,
	post_delete,
	)

urlpatterns = [
    url(r'^$', post_list, name="list"),
    url(r'^create/$', post_create),
    url(r'^content/(?P<slug>[\w-]+)/$', post_content, name="content"),
    url(r'^content/(?P<slug>[\w-]+)/edit/$', post_update, name="update"),
    url(r'^content/(?P<slug>[\w-]+)/delete/$', post_delete),
]