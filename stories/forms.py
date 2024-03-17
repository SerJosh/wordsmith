from django import forms
from django.forms import ModelForm
from .models import Story
from django_summernote.widgets import SummernoteWidget


class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ('Title', 'Blurb', 'Content', 'Story_Cover', )

        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control w-25  text-center'}),
            'Blurb': forms.Textarea(attrs={'class': 'form-control w-50 text-center', "rows":4, "cols":10}),
            'Content': forms.TextInput(attrs={'class': 'form-control'})
        }

    Content = forms.CharField(widget=SummernoteWidget)