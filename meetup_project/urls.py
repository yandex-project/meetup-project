from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('meetup/', include('meetups.urls')),
    path('search/', include('search.urls')),
    path('schedule/', include('schedule.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('auth/', include('users.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('djeym/', include('djeym.urls', namespace='djeym')),
    path('map/', include('maps.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'homepage.views.error_404_view'
handler500 = 'homepage.views.error_500_view'
