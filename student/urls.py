from django.urls import re_path
from .import views

app_name = 'student'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^add/$', views.addStudent, name='add')
]
