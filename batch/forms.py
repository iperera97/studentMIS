from django import forms
from .models import Batch


class BatchForm(forms.ModelForm):

    class Meta:
        model = Batch
        exclude = ['register', 'course', 'slug']
