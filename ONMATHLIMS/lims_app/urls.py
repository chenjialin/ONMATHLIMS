from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'project_input', views.project_input),
    url(r'welcome', views.welcome, name='welcome'),
    url(r'main', views.main, name='main'),
    url(r'receive_sample', views.receive_sample, name='receive_sample'),
]