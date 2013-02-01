from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, ModelChoiceField
from django.utils.translation import ugettext_lazy as _
from main.models import *


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet

class KeywordForm(forms.ModelForm):
    class Meta:
        model = Query

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

