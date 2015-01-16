from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import HelloWorldView


urlpatterns = patterns(
    '',

    url(r'^$', HelloWorldView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
