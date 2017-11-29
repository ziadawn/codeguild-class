from django.conf.urls import url

from . import views         # the . designates the current directory

app_name = 'todo'

urlpatterns = [
    url(r'^$', views.index, name='index'),       # this is our app's route
    url(r'^savetodo/$', views.savetodo, name='savetodo')
]
