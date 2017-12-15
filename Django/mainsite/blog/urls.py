from django.conf.urls import url

from . import views         # the . designates the current directory

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),       # this is our app's route
    url(r'^post_detail/(?P<post_id>\d+)$', views.post_detail, name='post_detail'),
    url(r'^write_post/$', views.write_post, name='write_post')
]
