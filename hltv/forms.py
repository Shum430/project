from .models import *

from django.forms import Form, CharField, TextInput,ModelForm


class MatchCommentForm(Form):
    text=CharField(label='comment',widget=TextInput(attrs={'placeholder':'your comment'}))


class TeamForm(ModelForm):
    class Meta:
        model=Team
        fields='__all__'

