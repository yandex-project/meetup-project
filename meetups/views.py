from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseNotFound

from meetups.models import Meetup, Lecture
from meetups.forms import LectureForm, MeetupForm


class CreateMeetupView(View):
    template_name = 'meetup/create_meetup/index.html'

    def get(self, request):
        form = MeetupForm()
        context = {
            'text': 'Добавление митапа',
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = MeetupForm(request.POST)
        if form.is_valid():
            new_meetup = Meetup.objects.create(
                name=form.cleaned_data['name'],
                date=form.cleaned_data['date'],
                description=form.cleaned_data['description'],
                place=form.cleaned_data['place'],
                website=form.cleaned_data['website'],
                is_visible=form.cleaned_data['is_visible'],
                owner=request.user
            )

            for tag in form.cleaned_data['tags']:
                new_meetup.tags.add(tag)

            new_meetup.save()
            return redirect('meetup_detail', new_meetup.slug)

        context = {
            'text': 'Добавление митапа',
            'form': form,
        }

        return render(request, self.template_name, context)


class UpdateMeetupView(View):
    template_name = 'meetup/create_meetup/index.html'

    def get(self, request, slug):
        meetup = Meetup.objects.get(slug=slug)

        if request.user != meetup.owner:
            return HttpResponseNotFound()

        form = MeetupForm(instance=meetup)
        context = {
            'text': 'Изменение митапа',
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request, slug):
        meetup = Meetup.objects.get(slug=slug)

        if request.user != meetup.owner:
            return HttpResponseNotFound()

        form = MeetupForm(request.POST, instance=meetup)
        if form.is_valid():
            meetup.name = form.cleaned_data['name']
            meetup.date = form.cleaned_data['date']
            meetup.description = form.cleaned_data['description']
            meetup.place = form.cleaned_data['place']
            meetup.website = form.cleaned_data['website']
            meetup.is_visible = form.cleaned_data['is_visible']

            # TODO: update tags

            meetup.save()
            return redirect('meetup_detail', meetup.slug)

        context = {
            'text': 'Изменение митапа',
            'form': form,
        }

        return render(request, self.template_name, context)


class MeetupDetailView(View):
    template_name = 'meetup/detail_page/index.html'

    def get(self, request, slug):
        context = {
            # TODO: add this query to manager
            'meetup': Meetup.objects.select_related('owner').select_related('marker').prefetch_related(
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
        lecture = meetup.lectures.get(pk=pk)

        if not (request.user == meetup.owner or request.user in lecture.lectors.all()):
            return HttpResponseNotFound()

        form = LectureForm(instance=lecture)

        context = {
            'meetup_name': meetup.name,
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, slug, pk):
        meetup = Meetup.objects.get(slug=slug)
        lecture = meetup.lectures.get(pk=pk)

        if not (request.user == meetup.owner or request.user in lecture.lectors.all()):
            return HttpResponseNotFound()

        form = LectureForm(data=request.POST, instance=lecture)

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
