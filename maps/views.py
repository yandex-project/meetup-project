from django.shortcuts import render
from django.views.generic import TemplateView, View
from maps.utils import get_global_map
from django.http import HttpResponse, HttpResponseForbidden
from maps.models import Placemark, Marker


# displays a global map of all meetups (added for testing)
class GlobalMapView(TemplateView):
    template_name = 'maps/global_map.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_slug'] = get_global_map().slug
        context['markers'] = Marker.objects.filter(placemark__active=True).values_list('id', flat=True)

        return context


#redefined class from djeym.views
class AjaxUploadPlacemarks(View):
    """Ajax - Upload placemarks to map."""

    def get(self, request, *args, **kwargs):
        markers = list(request.GET.getlist('markers[]'))
        offset = int(request.GET.get('offset'))
        limit = offset + 1000

        geoobjects = Placemark.objects.filter(marker__id__in=markers,
                                              active=True,
                                              ).values_list(
            'json_code', flat=True)[offset:limit]

        response_data = '[' + ','.join(geoobjects) + ']'

        return HttpResponse(response_data, content_type="application/json")

    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseForbidden()
        return super(AjaxUploadPlacemarks, self).dispatch(request, *args, **kwargs)
