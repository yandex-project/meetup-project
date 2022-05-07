from django.shortcuts import render
from django.views.generic import TemplateView
from maps.utils import get_global_map


# displays a global map of all meetups (added for testing)
class GlobalMapView(TemplateView):
    template_name = 'maps/global_map.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_slug'] = get_global_map().slug

        return context
