from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'project_input/', views.project_input),
    url(r'main/', views.main, name='main'),
    url(r'receive_sample/', views.receive_sample, name='receive_sample'),
    url(r'^$', views.login, name='login'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^project_view/', views.project_view, name='project_view'),
    url(r'^quality_check/', views.quality_check, name='quality_check'),
    url(r'^upload/', views.upload_file, name='upload'),
    url(r'^upload/(?P<table>\w+)/$', views.upload_file, name='upload'),
# url(r'get_sample_by_project', views.get_sample_by_project, name='get_sample_by_project'),
    url(r'get_sample_by_project2', views.get_sample_by_project2, name='get_sample_by_project2'),
]
