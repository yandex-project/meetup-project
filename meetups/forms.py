from meetups.models import Lecture
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
