from django.forms import ModelForm
from django.forms import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Booking, Time
from django.forms.fields import MultipleChoiceField


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['email'].widget.attrs['type'] = 'text'
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'

class CustomModelChoiceIterator(models.ModelChoiceIterator):
    def choice(self, obj):
        return (self.field.prepare_value(obj),
                self.field.label_from_instance(obj), obj)

class CustomModelChoiceField(models.ModelMultipleChoiceField):
    def _get_choices(self):
        if hasattr(self, '_choices'):
            return self._choices
        return CustomModelChoiceIterator(self)
    choices = property(_get_choices, MultipleChoiceField._set_choices)

class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['time']
        exclude = ['user', 'field', 'booking_code', 'timestamp']

    # time = CustomModelChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     queryset=Time.objects.all()
    # )
    # time = forms.ModelMultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     queryset=Time.objects.all()
    # )