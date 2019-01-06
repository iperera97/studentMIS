from django.contrib import admin
from django.urls import re_path, include, path
from .import views


urlpatterns = [
    path('', views.home, name='homepage'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^auth/', include('authentication.urls')),
    re_path(r'^dashboard/', include('dashboard.urls')),
    re_path(r'^courses/', include('courses.urls')),
    re_path(r'^students/', include('student.urls')),
]
