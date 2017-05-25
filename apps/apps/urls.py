from django.conf.urls import include, url
from django.contrib import admin

import theme.views
import dziennik_posilkow.urls

urlpatterns = [
    url(r'^$', theme.views.home, name='home'),
    url(r'^dziennik_posilkow/', include(dziennik_posilkow.urls, namespace='dziennik_posilkow')),
    url(r'^admin/', include(admin.site.urls)),
]
