from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cats/', include('catservice.urls')),
    url(r'^catui/', include('catui.urls')),
    url(r'^twitter/', include('twitterservice.urls')),
    url(r'^d3/', include('d3.urls')),
]
