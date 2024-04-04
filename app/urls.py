from django.contrib import admin
from django.urls import include, path

from django.conf.urls.static import static
from app import settings
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace = 'main')),
    path('catalog/', include('goods.urls', namespace = 'catalog')),
    path('user/', include('users.urls', namespace = 'user')),
]


if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
     ]
    
    urlpatterns += static(settings.MEDIA_URL, document__root=settings.MEDIA_ROOT)