from django.urls import re_path
from .import views


app_name = "batch"

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    re_path(r"^create", views.createBatch, name="create"),
    re_path(r"^remove/(?P<batch_name>[-\w]+)/$",
            views.removeBatch, name='remove'),
    re_path(r"^edit/(?P<batch_name>[-\w]+)/$", views.editBatch, name='edit')
]
