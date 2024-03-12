from django import forms
from django_summernote.widgets import SummernoteWidget
from cloudinary.models import CloudinaryField

# class NameForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)

class StoryForm(forms.Form):
    Title = forms.CharField(max_length=20)
    featured_image = CloudinaryField('image', default='placeholder')
    Blurb = forms.CharField(max_length=200, widget=forms.Textarea )
    Story = forms.CharField(widget=SummernoteWidget)