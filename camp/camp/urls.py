"""camp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from timeapp.views import hello, time, time_diff, time_diff2, ttime, ttime_diff

from myapp.views import persons, details

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', hello),
    url(r'^time$', time),
    url(r'^time/plus/(\d{1,2})/$', time_diff),
    url(r'^time/add/(\d{1,2})/$', time_diff2),
    url(r'^time/template/$', ttime),
    url(r'^time/templates/(\d{1,2})/$', ttime_diff),
    url(r'^person$', persons),
    url(r'^persons/info/(\d{1,})$', persons)

]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^$', hello),
#     url(r'^time$', time),
#     url(r'^time/plus/(\d{1,2})/$', time_diff),
#     url(r'^time/add/(\d{1,2})/$', time_diff2),
#     url(r'^time/template/$', ttime),
#     url(r'^time/templates/(\d{1,2})/$', ttime_diff),
#
# ]
