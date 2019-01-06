from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import StudentForm, RegistrationFrom
from .models import Registration, Student


# student home
def home(request):

    parseData = {
        'title': 'Students',
        'pageTitle': ['Students']
    }

    # table & pagination
    student_list = Student.objects.get_queryset().order_by('pk')
    paginator = Paginator(student_list, 8)  # Show 25 contacts per page

    page = request.GET.get('page')
    eachPageStudent = paginator.get_page(page)

    parseData['student_list'] = eachPageStudent

    return render(request, 'student/home.html', parseData)


# student add
def addStudent(request):

    parseData = {
        'title': 'Student - Add',
        'pageTitle': ['Students', 'Add']
    }

    reg_config = {
        'form-TOTAL_FORMS': '2',
        'form-INITIAL_FORMS': '0',
        'form-MIN_NUM_FORMS': '',
        'form-MAX_NUM_FORMS': '',
    }

    # forms (when page load)
    student_form = StudentForm()
    RegistrationFormSet = modelformset_factory(
        Registration, form=RegistrationFrom, min_num=1, validate_min=True)

    if request.method == 'POST':

        # forms
        student_form = StudentForm(request.POST)
        registration_formset = RegistrationFormSet(request.POST)

        if student_form.is_valid() and registration_formset.is_valid():

            # register student
            student = student_form.save()
            registration = registration_formset.save(commit=False)

            # register course
            for register in registration:
                register.student_id = student.pk
                register.save()

            # flash msg
            messages.success(request, "(#{}) {} {} successfully added student".format(
                student.pk, student.title, student.first_name
            ))

            return redirect('student:home')
        else:
            # show errors
            print(registration_formset.errors)
    else:
        registration_formset = RegistrationFormSet(reg_config)

    parseData['student_form'] = student_form
    parseData['registration_formset'] = registration_formset

    return render(request, 'student/add.html', parseData)
