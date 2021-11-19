from django import forms
from .models import *

#form for the poll with widgets
class PollForm(forms.ModelForm):

    class Meta():
        model = Poll
        fields = ('title',)

class AnswerForm(forms.ModelForm):

    class Meta():
        model = Answer
        fields = ('poll', 'title', 'isRequired')
