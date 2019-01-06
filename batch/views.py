from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from .decorators import check_valid_course, check_valid_batch
from django.contrib import messages
from django.http import Http404
from .forms import BatchForm
from .models import Batch


# batch home
@check_valid_course
def home(request, *args, **kwargs):

    page = request.GET.get('page')

    parseData = {
        'title': '{} - Batches'.format(kwargs['course_name'].replace('-', ' ').upper()),
        'pageTitle': ['(#{}) {}'.format(kwargs['course_id'], kwargs['course_name'].replace("-", " ")), 'Batches'],
        'courseName': kwargs['course_name'].replace("-", " "),
        'course_slug': kwargs['course_name'],
    }

    # form
    batchform = BatchForm()
    parseData['batchform'] = batchform

    # table
    batchListQuery = Batch.objects.filter(
        course__id=kwargs['course_id']).order_by('pk')
    paginator = Paginator(batchListQuery, 10)
    parseData['batchList'] = paginator.get_page(page)

    return render(request, 'batch/home.html', parseData)


# create batch
@check_valid_course
def createBatch(request, *args, **kwargs):

    parseData = {}

    if request.method == 'POST' and request.is_ajax():

        batch_form = BatchForm(request.POST)

        # form is valid
        if batch_form.is_valid():

            batchInstance = batch_form.save(commit=False)
            batchInstance.course_id = kwargs['course_id']

            try:

                batchInstance.save()  # save record

            except Exception as err:

                batch_form.add_error(
                    'name', 'Batch name is allready exsits to this course')
                parseData['errors'] = batch_form.errors.get_json_data()
            else:

                # unsuccess
                if batchInstance.pk is None:

                    parseData['status'] = False
                    parseData['msg'] = 'batch not found'

                else:
                    # success
                    parseData['status'] = True
                    parseData['msg'] = 'batch has successfully created'

        else:
            parseData['status'] = False
            parseData['errors'] = batch_form.errors.get_json_data()
    else:

        parseData['status'] = False
        parseData['msg'] = 'please request this url with post or ajax'

    print(parseData)
    return JsonResponse(parseData)


# remove batch
@check_valid_course
@check_valid_batch
def removeBatch(request, *args, **kwargs):

    deleteResponse = Batch.objects.get(pk=kwargs['batch_id']).delete()

    if deleteResponse[0] == 0:
        raise Http404('cannot delete this record right now')
    else:
        messages.success(
            request, '(#{}) {} batch was successfully removed'.format(kwargs['batch_id'], kwargs['batch_name']))
        return redirect('courses:batch:home', course_name=kwargs['course_name'])


@check_valid_course
@check_valid_batch
def editBatch(request, *args, **kwargs):

    parseData = {}

    # get relevent batch and create form
    getBatch = Batch.objects.get(pk=kwargs['batch_id'])
    batchForm = BatchForm(instance=getBatch)

    if request.method == 'POST':
        batchForm = BatchForm(request.POST, instance=getBatch)

        if batchForm.is_valid():

            try:
                batchInstance = batchForm.save()
            except Exception as err:

                batchForm.add_error(
                    'name', 'Batch name is allready exsits')

            else:
                messages.success(request, "(#{}) {} successufully edited".format(
                    batchInstance.pk, batchInstance.name))
                return redirect('courses:batch:home', course_name=kwargs['course_name'])

        else:
            print(False)

    # parsing data
    parseData['batchForm'] = batchForm

    return render(request, 'batch/edit.html', parseData)
