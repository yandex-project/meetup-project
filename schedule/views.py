from django.shortcuts import render
from django.views import View

from meetups.models import Meetup


class ScheduleView(View):
    template_name = 'schedule/index.html'

    def get(self, request):
        context = {'items': Meetup.objects.filter(is_visible=True)}

        return render(request, self.template_name, context)

    def post(self, request):
        context = {'items': Meetup.objects.filter(is_visible=True)}

        return render(request, self.template_name, context)
