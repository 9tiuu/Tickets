from django.contrib import admin
from django.urls import path, include
from tickets import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tickets/', include('tickets.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
