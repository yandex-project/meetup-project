from django.shortcuts import render
from django.views import View


class SearchView(View):
    template_name = 'search/index.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
