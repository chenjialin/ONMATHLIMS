from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'project_input', views.project_input),
    url(r'welcome', views.welcome, name='welcome'),
]