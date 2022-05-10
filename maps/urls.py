from django.urls import path
from maps import views


urlpatterns = [
    path('', views.GlobalMapView.as_view(), name='global_map'),
    path('ajax-upload-placemarks/',
         views.AjaxUploadPlacemarks.as_view(),
         name='ajax_get_geo_objects_placemark'),
]