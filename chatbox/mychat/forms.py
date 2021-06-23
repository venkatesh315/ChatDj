from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from captcha.fields import CaptchaField


class CaptchaUserCreationForm(UserCreationForm):

    captcha = CaptchaField()


class EditPofileForm(UserChangeForm):

    class Meta:
        model= User
        fields=(
            'username',
            'email',
            'first_name',
            'last_name',

        )