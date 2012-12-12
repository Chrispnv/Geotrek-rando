from django.conf.urls import patterns, include, url
from .views import HomeView, TrekView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^(?P<slug>[-\w]+)$', TrekView.as_view(), name="detail"),
)