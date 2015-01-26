from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HelloWorldView

from bookmarks.views import (BookmarkCreateView, BookmarkListView,
                             BookmarkUpdateView, BookmarkDeleteView)


urlpatterns = patterns(
    '',
    url(r'^$', BookmarkListView.as_view(), name='bookmark-list'),

    url(r'^hello/$', HelloWorldView.as_view()),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^create/$', BookmarkCreateView.as_view()),
    url(r'^list/$', BookmarkListView.as_view(), name='bookmark-list'),

    url(r'^update/(?P<pk>\d+)/$', BookmarkUpdateView.as_view(),
        name='bookmark-update'),
    url(r'^delete/(?P<pk>\d+)/$', BookmarkDeleteView.as_view(),
        name='bookmark-delete'),
)
