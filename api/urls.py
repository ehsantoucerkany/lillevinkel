from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
