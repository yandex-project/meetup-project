from django.db.models import Prefetch
from django.shortcuts import render
from django.views import View

from meetups.models import Meetup, Lecture


class MeetupDetailView(View):
    template_name = 'meetup/index.html'

    def get(self, request, slug):
        context = {
            # TODO: add this query to manager
            'meetup': Meetup.objects.select_related('owner').prefetch_related(
                Prefetch(
                    'lectures',
                    Lecture.objects.prefetch_related(
                        'lectors'
                    )
                )
            ).get(slug=slug)
        }

        return render(request, self.template_name, context)
