from django.shortcuts import render
from django.views import View

from meetups.models import Meetup, Tag


class SearchView(View):
    template_name = 'search/index.html'

    def get(self, request):
        context = {
            'items': Meetup.objects.filter(is_visible=True),
            'tags': Tag.objects.all().order_by('name')
        }

        return render(request, self.template_name, context)

    def post(self, request):
        context = {
            'items': Meetup.objects.filter(is_visible=True),
            'tags': Tag.objects.all().order_by('name')
        }

        return render(request, self.template_name, context)
