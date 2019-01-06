from django.urls import re_path
from .import views

app_name = 'auth'

urlpatterns = [
    re_path(r'^login/$', views.loginUser, name='login'),
    re_path(r'^logout/$', views.logoutUser, name='logout')
]
