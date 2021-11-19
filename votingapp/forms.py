from django import forms
from .models import *

#form for the poll with widgets
class PollForm(forms.ModelForm):

    class Meta():
        model = Poll
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs= {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea poll content'})
        }
