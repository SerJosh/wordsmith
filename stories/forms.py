from django import forms
from django.forms import ModelForm
from .models import Story
from django_summernote.widgets import SummernoteWidget

# class NameForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)

# class StoryForm(forms.Form):
#     Title = forms.CharField(max_length=20)
#     Blurb = forms.CharField(max_length=200, widget=forms.Textarea )
#     Story = forms.CharField(widget=SummernoteWidget)

# Create Story Form
class StoryForm(ModelForm):
    class Meta:
        model = Story
        fields = ('Title', 'Blurb', 'Content', 'Story_Cover', )

        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Blurb': forms.TextInput(attrs={'class': 'form-control'}),
            'Content': forms.TextInput(attrs={'class': 'form-control'})
        }

    Content = forms.CharField(widget=SummernoteWidget)