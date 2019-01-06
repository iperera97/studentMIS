from django.shortcuts import render
from courses.models import Course
from batch.models import Batch
from student.models import Student


def dashboard(request):

    parseData = {
        'title': 'Dashboard',
        'pageTitle': ['dashboard']
    }

    studentCount = Student.objects.all().count()
    courseCount = Course.objects.all().count()
    batchCount = Batch.objects.filter(active=True).count()

    parseData['model_count'] = {
        'student': studentCount,
        'course': courseCount,
        'batch': batchCount
    }

    return render(request, 'dashboard/home.html', parseData)
