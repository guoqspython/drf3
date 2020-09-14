
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.static import serve

from drf3 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    path("api/",include("api.urls"))
]
