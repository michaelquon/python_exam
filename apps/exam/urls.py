from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^create$', views.create),
    url(r'^show/(?P<wish_id>\d+)', views.show),
    url(r'^add$', views.add),
    url(r'^addWish$', views.addWish),
    url(r'^createJoin/(?P<wish_id>\d+)', views.createJoin),
    url(r'^delete$', views.delete),
    url(r'^destroy/(?P<wish_id>\d+)$', views.destroy)
    

]