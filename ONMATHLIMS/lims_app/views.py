# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import DbObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from forms import SampleProjectMasterForm, UserForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from models import UserInfo, SampleProjectMaster

import os
import json
# Create your views here.
CODE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def login(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            username = request.POST.get('username', '')
            response = HttpResponseRedirect('/lims_app/main/')
            response.set_cookie('username', username, 3600)
            return response
    else:
        user_form = UserForm()
    return render(request, 'login.html', {'user_form': user_form})


def logout(request):
    response = HttpResponseRedirect('/lims_app/login/')
    response.delete_cookie('username')
    return response


def project_input(request):
    if request.method == "POST":
        form = SampleProjectMasterForm(request.POST)
        if form.is_valid():
            project = form.save()
            project.save()
            return HttpResponseRedirect(reverse("welcome"))
    else:
        form = SampleProjectMasterForm()
    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'project_input.html'), {'form': form})


def main(request):
    username = request.COOKIES.get('username', '')
    all_projects = SampleProjectMaster.objects.all()
    all_projects_list = []
    for each_project in all_projects:
        project_dict = {}
        project_dict['id'] = each_project.id
        project_dict['project_number'] = each_project.project_number
        project_dict['create_time'] = each_project.create_time.split(" ")[0]
        project_dict['status'] = each_project.status
        project_dict['cust_user'] = each_project.cust_user
        all_projects_list.append(project_dict)
    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'index.html'),
                  {'username': username, 'all_projects': all_projects_list})


def receive_sample(request):
    username = request.COOKIES.get('username', '')
    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'receive_sample.html'),
                  {'username': username})


def project_view(request):
    msg = 'request is not post!'
    if request.method == 'POST':
        project_master_info = {}
        for key, value in request.POST.items():
            project_master_info[key] = value

        if project_master_info['action'] == 'edit':
            new_project_master_info = SampleProjectMaster(id=project_master_info['id'],
                                                          project_number=project_master_info[u'项目编号'],
                                                          cust_user=project_master_info[u'客户名称'],
                                                          status=project_master_info[u'状态'],
                                                          create_time=project_master_info[u'创建时间'])
            new_project_master_info.save()
            msg = 'update success!'
        elif  project_master_info['action'] == 'delete':
            try:
                old_project_master_info = SampleProjectMaster.objects.get(id=project_master_info['id'])
                old_project_master_info.delete()
            except DbObjectDoesNotExist, e:
                msg = 'nothing to delete!'
            msg = 'delete success!'
        else:
            msg = 'do nothing!'
    return HttpResponse({json.dumps(msg)})
