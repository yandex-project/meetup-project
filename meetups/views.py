from django.shortcuts import render
from django.views import View

from meetups.models import Meetup


class MeetupDetailView(View):
    template_name = 'meetup/index.html'

    def get(self, request, slug):
        context = {
            'meetup': Meetup.objects.get(slug=slug)
        }

        return render(request, self.template_name, context)
