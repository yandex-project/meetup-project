from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views import View
from django.urls import reverse

from meetups.models import Meetup, Tag


class SearchView(View):
    template_name = 'search/index.html'

    def get(self, request):
        if request.GET.get('map'):
            url = reverse('global_map')
            return HttpResponseRedirect(url + '?' + request.META['QUERY_STRING'])
        context = {
            'items': Meetup.objects.get_meetups_from_context(request.GET),
            'tags': Tag.objects.all().order_by('name')
        }

        return render(request, self.template_name, context)

    def post(self, request):
        context = {
            'items': Meetup.objects.filter(is_visible=True),
            'tags': Tag.objects.all().order_by('name')
        }

        return render(request, self.template_name, context)
