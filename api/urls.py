from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from webshop import views as webshop_views

router = routers.DefaultRouter()
router.register(r'products', webshop_views.ProductViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('authemail.urls')),
)
