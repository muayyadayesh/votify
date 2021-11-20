from django import forms
from .models import *

#form for the poll with widgets
class PollForm(forms.ModelForm):

    class Meta():
        model = Poll
        fields = ('title',)
