from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^(?P<screen_name>\w+)/friends$', views.friends),
    url(r'^$', views.index),
    url(r'^authenticated/$', views.authenticated),

]
