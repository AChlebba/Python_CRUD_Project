from django.conf.urls import patterns, url

from dziennik_posilkow import views

urlpatterns = [
  url(r'^$', views.home, name='home'),

  url(r'^zawodnik_view/(?P<pk>\d+)$', views.zawodnik_view, name='zawodnik_view'),
  url(r'^zawodnik_new$', views.zawodnik_create, name='zawodnik_new'),
  url(r'^zawodnik_edit/(?P<pk>\d+)$', views.zawodnik_update, name='zawodnik_edit'),
  url(r'^zawodnik_delete/(?P<pk>\d+)$', views.zawodnik_delete, name='zawodnik_delete'),

  url(r'^posilek_new/(?P<parent_pk>\d+)$', views.posilek_create, name='posilek_new'),
  url(r'^posilek_edit/(?P<pk>\d+)$', views.posilek_update, name='posilek_edit'),
  url(r'^posilek_delete/(?P<pk>\d+)$', views.posilek_delete, name='posilek_delete'),
]