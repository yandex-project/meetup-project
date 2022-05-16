from meetups.models import Lecture, Meetup
from django import forms
from users.forms import BaseForm


class LectureForm(forms.ModelForm, BaseForm):
    class Meta:
        model = Lecture
        fields = (
            'name',
            'time',
            'description',
            'lectors',
        )


class MeetupForm(forms.ModelForm, BaseForm):
    class Meta:
        model = Meetup
        fields = (
            'name',
            'date',
            'description',
            'place',
            'website',
            'tags',
            'is_visible',
        )
