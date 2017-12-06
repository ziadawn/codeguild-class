from django.conf.urls import url

from . import views

app_name = 'library'

urlpatterns = [
    url(r'^$', views.index, name='index'),        # creating route to index views
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^checkout_history/$', views.checkout_history, name='checkout_history')
]