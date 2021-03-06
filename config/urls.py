# djauth/urls.py
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.authorization.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('greenhouse/', include('apps.greenhouse.urls')),
    path('lab/', include('apps.lab.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  