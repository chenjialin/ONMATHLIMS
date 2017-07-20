from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'project_input', views.project_input),
    url(r'welcome', views.welcome, name='welcome'),
    url(r'main', views.main, name='main'),
    url(r'receive_sample', views.receive_sample, name='receive_sample'),
    # url(r'get_sample_by_project', views.get_sample_by_project, name='get_sample_by_project'),
    url(r'get_sample_by_project2', views.get_sample_by_project2, name='get_sample_by_project2'),
]