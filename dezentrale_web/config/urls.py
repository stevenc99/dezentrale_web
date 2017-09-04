# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from dezentrale_web.apps.wagtail_search import views as search_views
from dezentrale_web.apps.TempPages import views as temp_views
urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^django-admin/', include(admin.site.urls)),
    # Wagtail
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    #url(r'^search/$', search_views.search, name='search'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'^wagtail', include(wagtail_urls)),
    url(r'', temp_views.default),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
