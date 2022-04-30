from django.shortcuts import render


def homepage(request):
    template_name = 'homepage/index.html'
    context = {}

    return render(request, template_name, context)
