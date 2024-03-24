from django import forms
from django.forms import ModelForm
from .models import Story
# from django_summernote.widgets import SummernoteWidget


class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'auther', 'blurb', 'content', 'story_cover', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control title text-center mx-auto', 'placeholder':"Your Title here"}),
            'blurb': forms.Textarea(attrs={'class': 'form-control blurb mx-auto', "rows":4, "cols":10, 'placeholder':"Your Blurb here"}),
            'content': forms.Textarea(attrs={'class': 'form-control content mx-auto', "rows":20, "cols":1000, 'placeholder':"Your Story here"})
        }

    # Content = forms.CharField(widget=SummernoteWidget)