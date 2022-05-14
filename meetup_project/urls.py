from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from maps.views import AjaxUploadPlacemarks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('search/', include('search.urls')),
    path('schedule/', include('schedule.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('auth/', include('users.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path(
        'djeym/ajax-upload-placemarks/',
        AjaxUploadPlacemarks.as_view(),
        name='ajax_get_geo_objects_placemark'
    ),
    # переопределенный класс из djeym (чтобы добавить сортировку меток)
    path('djeym/', include('djeym.urls', namespace='djeym')),
    path('map/', include('maps.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
