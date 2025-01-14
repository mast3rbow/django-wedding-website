from django.conf.urls import include
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path("", include('wedding.urls')),
    path("", include('guests.urls')),
    path("admin/", admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls'))
]
