from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.db import models
from .import forms
from .models import Course
from batch.decorators import check_valid_course


# course home page
def courseHome(request):

    parseData = {
        'title': 'Course',
        'pageTitle': ['courses']
    }

    # create couse form
    createCouresForm = forms.CoursForm()
    parseData['createCouresForm'] = createCouresForm

    # table & pagination
    course_list = Course.objects.get_queryset().order_by('id')
    paginator = Paginator(course_list, 5)  # Show 10 contacts per page

    page = request.GET.get('page')
    eachPageCoures = paginator.get_page(page)

    # parseData['course_list'] = course_list
    parseData['course_list'] = eachPageCoures

    return render(request, 'courses/home.html', parseData)


# create course
def createCourse(request):

    # check is this a ajax request
    if request.is_ajax() and request.method == 'POST':

        # create form
        createCourseForm = forms.CoursForm(request.POST or None)
        parseData = {}

        if createCourseForm.is_valid():

            # parseData['status'] = True
            # parseData['msg'] = ['successfully form is valid']

            course = createCourseForm.save()

            # unsuccess
            if course.id is None:

                parseData['status'] = False
                parseData['msg'] = 'course is none'
            else:
                # successfully create a course

                parseData['status'] = True
                parseData['msg'] = 'course has successfully created'

        else:
            errors = createCourseForm.errors.get_json_data(escape_html=False)

            parseData['status'] = False
            parseData['errors'] = errors

    return JsonResponse(parseData)


# edit course (view)
@check_valid_course
def editCourse(request, *args, **kwargs):

    parseData = {
        'title': 'Course - {}'.format(kwargs['course_name']),
        'pageTitle': ['Edit Course', kwargs['course_name'].replace("-", " ")]
    }

    course = Course.objects.get(pk=kwargs['course_id'])

    if request.method == 'GET':

        courseEditForm = forms.CoursForm(instance=course)
    else:
        courseEditForm = forms.CoursForm(request.POST, instance=course)

        if courseEditForm.is_valid():

            editedCourse = courseEditForm.save()

            # unsuccess
            if editedCourse is None:
                pass  # do validation part
            else:
                # success
                editMsg = "(#{}) {} has been successfully edited".format(
                    course.pk, course.title)

                messages.success(request, editMsg)
                return redirect('courses:home')

    # form
    parseData['courseEdit'] = courseEditForm

    return render(request, 'courses/edit.html', parseData)


# delete course
@check_valid_course
def deleteCourse(request, *args, **kwargs):

    course = Course.objects.get(pk=kwargs['course_id'])

    courseID = course.pk
    courseTitle = course.title

    deleteResponse = course.delete()

    # if not delete
    if deleteResponse[0] == 0:

        errMsgOnDelete = "(#{}) {} has been removed".format(
            courseID, courseTitle)
        messages.success(request, errMsgOnDelete)
    else:
        # successfully delete

        successMsgOndelete = "(#{}) {} has been removed".format(
            courseID, courseTitle)
        messages.success(request, successMsgOndelete)

    return redirect('courses:home')


# view each Course
@check_valid_course
def viewEachCource(request, *args, **kwargs):

    parseData = {
        'title': 'Course - {}'.format(kwargs['course_name']),
        'pageTitle': ['View Course', kwargs['course_name'].replace("-", " ")]
    }

    course = Course.objects.get(pk=kwargs['course_id'])
    parseData['course'] = course

    return render(request, 'courses/course.html', parseData)
