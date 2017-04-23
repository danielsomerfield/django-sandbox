from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^health$', views.health),
    url(r'^(?P<cat_name>\w+)/pet$', views.pet),
    url(r'^(?P<cat_name>\w+)/brush', views.brush),
    url(r'^foo', views.foo),

]
