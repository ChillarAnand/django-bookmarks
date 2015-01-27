from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HelloWorldView

from bookmarks.views import (create_bookmark, list_bookmarks,
                             edit_bookmark, delete_bookmark)


urlpatterns = patterns(
    '',

    url(r'^hello/$', HelloWorldView.as_view()),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^create/$', create_bookmark, name='create_bookmark'),
    url(r'^list/$', list_bookmarks, name='list_bookmarks'),
    url(r'^edit/(?P<bookmark_id>\d+)$', edit_bookmark, name='edit_bookmark'),
    url(r'^delete/(?P<bookmark_id>\d+)$', delete_bookmark,
        name='delete_bookmark'),

    # url(r'^list/$', BookmarkListView.as_view(), name='bookmark-list'),

    #     url(r'^update/(?P<pk>\d+)/$', BookmarkUpdateView.as_view(),
    #         name='bookmark-update'),
    #     url(r'^delete/(?P<pk>\d+)/$', BookmarkDeleteView.as_view(),
    #         name='bookmark-delete'),
)
