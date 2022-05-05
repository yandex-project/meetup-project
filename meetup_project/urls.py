from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('search/', include('search.urls')),
    path('schedule/', include('schedule.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('auth/', include('users.urls')),
]
