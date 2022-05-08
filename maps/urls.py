from django.urls import path
from maps import views


urlpatterns = [
    path('', views.GlobalMapView.as_view(), name='global_map')
]