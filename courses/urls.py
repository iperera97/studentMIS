from django.urls import re_path, include
from .import views

app_name = 'courses'

urlpatterns = [
    re_path(r'^$', views.courseHome, name='home'),
    re_path(r'^create/$', views.createCourse, name='create'),
    re_path(r'^edit/(?P<course_name>[-\w]+)/$', views.editCourse, name='edit'),
    re_path(r'^delete/(?P<course_name>[-\w]+)/$',
            views.deleteCourse, name='delete'),
    re_path(r'^(?P<course_name>[-\w]+)/$', views.viewEachCource, name='view'),
    re_path(r'^(?P<course_name>[-\w]+)/batch/', include('batch.urls'))
]
