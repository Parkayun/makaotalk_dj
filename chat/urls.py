from django.conf.urls import url

from .views.web import index


urlpatterns = [
    url(r'^$', index, name='web_index'),
]
