# bid_intelligence_system/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='marketing/home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('apps.projects.urls')),
    path('api/', include('apps.api.urls')),
    path('subscriptions/', include('apps.subscriptions.urls')),
    path('bids/', include('apps.bids.urls')),  # Add this line to include bids URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)