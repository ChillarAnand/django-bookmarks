from django import forms

from .models import Folder


class BookmarkForm(forms.Form):
    name = forms.CharField(max_length=100)
    url = forms.URLField()
    description = forms.CharField(max_length=200)
    folder = forms.ModelChoiceField(queryset=Folder.objects.all())


class DeleteForm(forms.Form):
    pass
