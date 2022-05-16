from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseNotFound

from meetups.models import Meetup, Lecture
from meetups.forms import LectureForm


class MeetupDetailView(View):
    template_name = 'meetup/detail_page/index.html'

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


class CreateLectureView(View):
    template_name = 'meetup/add_lecture/index.html'

    def get(self, request, slug):
        meetup = Meetup.objects.get(slug=slug)
        if request.user != meetup.owner:
            return HttpResponseNotFound()

        form = LectureForm()
        context = {
            'meetup_name': meetup.name,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, slug):
        meetup = Meetup.objects.get(slug=slug)
        if request.user != meetup.owner:
            return HttpResponseNotFound()

        form = LectureForm(request.POST)
        if form.is_valid():
            new_lecture = Lecture.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                time=form.cleaned_data['time'],
                meetup=meetup
            )
            # TODO: Посмотреть возможно ли по-другому
            for lector in form.cleaned_data['lectors']:
                new_lecture.lectors.add(lector)
            new_lecture.save()

            return redirect('meetup_detail', slug)
        context = {
            'meetup_name': meetup.name,
            'form': form
        }
        return render(request, self.template_name, context)


class UpdateLectureView(View):
    template_name = 'meetup/add_lecture/index.html'

    def get(self, request, slug, pk):
        meetup = Meetup.objects.get(slug=slug)
        if request.user != meetup.owner:
            return HttpResponseNotFound()

        lecture = meetup.lectures.get(pk=pk)
        form = LectureForm(instance=lecture)

        context = {
            'meetup_name': meetup.name,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, slug, pk):
        meetup = Meetup.objects.get(slug=slug)
        if request.user != meetup.owner:
            return HttpResponseNotFound()
        lecture = meetup.lectures.get(pk=pk)
        form = LectureForm(data=request.POST)

        if form.is_valid():
            lecture.name = form.cleaned_data['name']
            lecture.description = form.cleaned_data['description']
            lecture.time = form.cleaned_data['time']

            # TODO: update lectors

            lecture.save()

            return redirect('meetup_detail', slug)

        context = {
            'meetup_name': meetup.name,
            'form': form
        }

        return render(request, self.template_name, context)
