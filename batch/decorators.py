from courses.models import Course
from batch.models import Batch
from django.http import Http404


# check course name is valid and get relevent course id
def check_valid_course(func):

    def wrapper(request, *args, **kwargs):

        getCourse = Course.objects.filter(
            slug=kwargs['course_name']).values('id')

        # success
        if getCourse:
            kwargs['course_id'] = getCourse[0]['id']
            return func(request, *args, **kwargs)
        else:
            # unsuccess
            raise Http404("{} that course not found".format(
                kwargs['course_name']))

    return wrapper


# check batch is valid and get relevent batch id
def check_valid_batch(func):

    def wrapper(request, *args, **kwargs):

        getBatch = Batch.objects.filter(
            slug=kwargs['batch_name']).values('id', 'name')

        # unsuccess
        if not getBatch:
            raise Http404('{} batch not found'.format(kwargs['batch_name']))
        else:
            # success
            kwargs['batch_id'] = getBatch[0]['id']
            return func(request, *args, **kwargs)

    return wrapper
