from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from astro_objects.views import index

urlpatterns = [
    path('admin/', admin.site.urls),              # Маршрут административной панели
    path('', index, name='index'),               # Главная страница
    path('objects/', include('astro_objects.urls')),  # Подключаем основные маршруты
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

