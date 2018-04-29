from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),
    # Home App
    path('', include('home_app.urls')),
    # Desk App
    path('desk/', include('desk_app.urls')),
    # Profile App
    path('profile/', include('profile_app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
