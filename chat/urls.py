from django.conf.urls import url

from .views.web import create, index


urlpatterns = [
    url(r'^$', index, name='web_index'),

    url(r'^chat/create/$', create, name='web_create'),
]
