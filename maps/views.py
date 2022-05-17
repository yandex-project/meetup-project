from django.views.generic import TemplateView, View
from maps.utils import get_global_map
from django.http import HttpResponse, HttpResponseForbidden
from meetups.models import Meetup
from urllib.parse import unquote
from json import loads


# displays a global map of all meetups (added for testing)
# can use search filters like this: /map?name=value&...
class GlobalMapView(TemplateView):
    template_name = 'maps/global_map.html'

    def get(self, request, *args, **kwargs):
        ctx = dict()
        for i in request.GET:
            ctx[i] = request.GET.get(i)
        return super().get(request, *args, ctx=ctx, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_slug'] = get_global_map().slug
        context['filters'] = kwargs['ctx'] or {}

        return context


# redefined class from djeym.views
class AjaxUploadPlacemarks(View):
    """Ajax - Upload placemarks to map."""

    def get(self, request, *args, **kwargs):
        ctx = unquote(request.GET.get('filters'))
        ctx = loads(ctx)
        offset = int(request.GET.get('offset'))
        limit = offset + 1000

        geoobjects = Meetup.objects.get_meetups_from_context(ctx)
        geoobjects = geoobjects.values_list('marker__placemark__json_code',
                                            flat=True)[offset:limit]

        response_data = '[' + ','.join(geoobjects) + ']'

        return HttpResponse(response_data, content_type="application/json")

    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseForbidden()
        return super(AjaxUploadPlacemarks, self).dispatch(request, *args, **kwargs)
