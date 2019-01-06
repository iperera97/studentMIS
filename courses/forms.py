from django import forms
from .import models


# course form
class CoursForm(forms.ModelForm):

    class Meta:
        model = models.Course
        exclude = ['register', 'slug']
