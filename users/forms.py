from django.contrib.auth.forms import UserCreationForm

from users.models import User
from django import forms


class BaseForm(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.widget_type == 'time':
                visible.subwidgets[0].parent_widget.input_type = 'time'

            if visible.widget_type == 'datetime':
                visible.subwidgets[0].parent_widget.input_type = 'datetime-local'

                # TODO: убери этот костыль
                # For render value in html
                if visible.initial:
                    visible.initial = str(visible.initial).replace(' ', 'T').split('+')[0]

            if visible.widget_type == 'date':
                visible.subwidgets[0].parent_widget.input_type = 'date'


class RegistrationForm(UserCreationForm, BaseForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class UserForm(forms.ModelForm, BaseForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'description',
            'email',
            'avatar',
        )
