from django.conf.urls import url

from . import views

app_name = 'shorturl'

urlpatterns = [
    url(r'^$', views.index, name='index'),        # start with just views.index
    url(r'^saveurl/$', views.longurl, name='saveurl'),
    url(r'^(?P<code>[\w\d]+)$', views.redirect, name='redirect'),
]
