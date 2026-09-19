
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pages.views import service_worker

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('pages.urls')),
    path('authentification/', include('authentification_app.urls')),
    path('administration/', include('manage_Admin.urls')),
    path('sw.js', service_worker, name='service_worker'),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

handler404='pages.views.notfound'
