from django import forms
from .models import Student, Registration
from courses.models import Course


# student form
class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['title', 'initals', 'first_name',
                  'last_name',  'gender', 'email']
        widgets = {
            'gender': forms.RadioSelect
        }


class RegistrationFrom(forms.ModelForm):

    class Meta:
        model: Registration
        fields = ['course', 'batch', 'reg_fee']

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(), empty_label='Course')
