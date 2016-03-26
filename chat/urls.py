from django.conf.urls import url

from .views.web import chat, create, index


urlpatterns = [
    url(r'^$', index, name='web_index'),

    url(r'^chat/(?P<room_id>\d+)/$', chat, name="web_chat"),
    url(r'^chat/create/$', create, name='web_create'),
]
