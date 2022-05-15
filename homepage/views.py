from django.shortcuts import render
from django.http import Http404


def homepage(request):
    template_name = 'homepage/index.html'
    context = {}

    return error_404_view(request, "asjkdjfh")
    return render(request, template_name, context)


def error_404_view(request, exception):
    template_name = 'errors/error_404.html'
    return render(request, template_name)


def error_500_view(request):
    template_name = 'errors/error_500.html'
    return render(request, template_name)
