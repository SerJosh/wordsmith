#from git
from django import forms
# from django.utils.safestring import mark_safe
from django.forms import ModelForm
from .models import WordsmithUser

# class DeleteUser(forms.Form):
#     delete_checkbox = forms.BooleanField(label=mark_safe('Are you sure you want to delete your account?'), required=True)
#     def __init__(self, *args, **kwargs):
#         super(DeleteUser, self).__init__(*args, **kwargs)
class ProfileForm(ModelForm):
    class Meta:
        model = WordsmithUser
        fields = ('Name', 'Bio', )

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Bio': forms.TextInput(attrs={'class': 'form-control'}),
        }