from django.conf.urls import patterns, include, url
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from webshop import views as webshop_views


router = routers.DefaultRouter()
router.register(r'products', webshop_views.ProductViewSet)
router.register(r'brands', webshop_views.BrandViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('authemail.urls')),
)

# NOT FOR PRODUCTION
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)