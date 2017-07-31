# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import json
import datetime

from . import DbObjectDoesNotExist, select_colums_dict
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import django_excel as excel
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from forms import SampleProjectMasterForm, UserForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from models import SampleProjectMaster, SampleInfoDetail, Attachment
from interface import search_result_ini, get_sample_info, common


reload(sys)
sys.setdefaultencoding('utf8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# Create your views here.
CODE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def login_required(func):
    """
    Check if already login
    """
    def _decorator(request, *args, **kwargs):
        username = request.COOKIES.get('username', '')
        if username:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/lims_app/login/')
    return _decorator


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


@login_required
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


def search(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response
    key_word = request.GET.get('q').strip()
    table_header, table_values = search_result_ini.get_search_result(key_word)

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'search_data.html'),
                  {'username': username, 'key_word': key_word, 'table_header': table_header,
                   'table_values': table_values, 'count': len(table_values)})


def main(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        # search on main page
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)
    else:
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


'''
def project_view(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

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
        elif project_master_info['action'] == 'delete':
            try:
                old_project_master_info = SampleProjectMaster.objects.get(id=project_master_info['id'])
                old_project_master_info.delete()
            except DbObjectDoesNotExist, e:
                msg = 'nothing to delete!'
            msg = 'delete success!'
        else:
            msg = 'do nothing!'
    return HttpResponse({json.dumps(msg)})
'''

'''
view function for onmathlims modules
'''


def receive_sample(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)

    project_id = request.GET.get('project_id', '') or 0
    all_proj_info = get_sample_info.get_all_proj_info()
    all_attachment = common.get_attachment(project_id, 'receive_sample')
    sample_info = get_sample_info.get_sample_by_project(project_id, name='receive_sample')
    select_proj = get_sample_info.get_proj_name_by_id(project_id)

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'receive_sample.html'),
                  {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                   'select_proj': select_proj, 'project_id': project_id, 'all_attachment': all_attachment})


def operation_log(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'operation_log.html'))


def quality_check(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

    project_id = request.GET.get('project_id', '') or 0
    all_proj_info = get_sample_info.get_all_proj_info()
    sample_info = get_sample_info.get_sample_by_project(project_id, name='quality_check')
    select_proj = get_sample_info.get_proj_name_by_id(project_id)
    all_attachment = common.get_attachment(project_id, 'quality_check')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'quality_check.html'),
                  {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                   'select_proj': select_proj, 'project_id': project_id, 'all_attachment': all_attachment})


def build_lib(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

    project_id = request.GET.get('project_id', '') or 0
    all_proj_info = get_sample_info.get_all_proj_info()
    sample_info = get_sample_info.get_sample_by_project(project_id, name='build_lib')
    select_proj = get_sample_info.get_proj_name_by_id(project_id)
    all_attachment = common.get_attachment(project_id, 'build_lib')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'build_lib.html'),
                    {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                     'select_proj': select_proj, 'project_id': project_id, 'all_attachment': all_attachment})


def upmachine(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

    project_id = request.GET.get('project_id', '') or 0
    all_proj_info = get_sample_info.get_all_proj_info()
    sample_info = get_sample_info.get_sample_by_project(project_id, name='upmachine')
    select_proj = get_sample_info.get_proj_name_by_id(project_id)
    all_attachment = common.get_attachment(project_id, 'upmachine')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'upmachine.html'),
                    {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                     'select_proj': select_proj, 'project_id': project_id, 'all_attachment': all_attachment})


def downmachine(request):
    username = request.COOKIES.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

    project_id = request.GET.get('project_id', '') or 0
    all_proj_info = get_sample_info.get_all_proj_info()
    sample_info = get_sample_info.get_sample_by_project(project_id, name='downmachine')
    select_proj = get_sample_info.get_proj_name_by_id(project_id)
    all_attachment = common.get_attachment(project_id, 'downmachine')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'downmachine.html'),
                    {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                     'select_proj': select_proj, 'project_id': project_id, 'all_attachment': all_attachment})


@login_required
def save_sample_info(request):
    table_name = request.GET.get('table')
    sample_id = request.POST['name']
    value = request.POST['value']
    if table_name == 'receive_sample':
        SampleInfoDetail.objects.filter(id=sample_id.replace('sample_id_', '')).update(sendsample_comment=value)
    elif table_name == 'quality_check':
        SampleInfoDetail.objects.filter(id=sample_id.replace('sample_id_', '')).update(qualitycheck_comment=value)
    elif table_name == 'build_lib':
        SampleInfoDetail.objects.filter(id=sample_id.replace('sample_id_', '')).update(lib_comment=value)
    elif table_name == 'upmachine':
        SampleInfoDetail.objects.filter(id=sample_id.replace('sample_id_', '')).update(upmachine_comment=value)
    elif table_name == 'downmachine':
        SampleInfoDetail.objects.filter(id=sample_id.replace('sample_id_', '')).update(downmachine_comment=value)

    return JsonResponse({'msg': 'ok'})


def down_sample_info(request):
    transform_title = {'quality_check': u'质检', 'receive_sample': u'送样', 'build_lib': u'建库',
                        'upmachine': u'上机', 'downmachine': u'下机'}

    table_name = request.GET.get('table', '')
    project_number = request.GET.get('project_number', '')
    if table_name and project_number:
        query_sets = SampleInfoDetail.objects.filter(project_number=project_number)
        column_names = select_colums_dict[table_name]
        return excel.make_response_from_query_sets(    #require excel module
            query_sets,
            column_names,
            'xls',
            file_name=project_number + transform_title[table_name] + u'结果'
        )
    else:
        JsonResponse({'msg': 'error'})


def save_table_data(request):
    json_data = request.POST['json_data']
    project_id = request.POST['project_id']
    json_data = json.loads(json_data)
    # delete old data, 这里不应该做物理删除， 应该用一个字段来代表 记录被删除， 当显示的时候， 我们对其进行过滤就行了， 请设计相应字段(ง •̀_•́)ง
    SampleInfoDetail.objects.filter(project_id=project_id).delete()

    # insert new data
    for row_dict in json_data:
        SampleInfoDetail.objects.create(sample_name=row_dict['样品名称'],
                                        express_number=row_dict['样品名称'],
                                        product_num=row_dict['管数'],
                                        sendsample_time=row_dict['修改日期'],
                                        sendsample_comment=row_dict['样品备注'])

    return redirect('/lims_app/receive_sample/?project_id=%s' % project_id)


def upload_attachment(request):
    username = request.COOKIES.get('username', '')
    file_name = request.GET.get("file_name").rsplit('\\')[-1]
    file_type = request.GET.get("type")
    project_id = request.GET.get("project_id")
    user_id = get_sample_info.get_user_id_by_name(username)
    content = request.FILES['file']
    file_path = 'lims_app' + os.path.sep + 'static' + os.path.sep + 'attachment' + os.path.sep + str(project_id)\
                + os.path.sep + file_type
    full_file_name = file_path + os.path.sep + file_name
    if not os.path.exists(file_path):
        os.system('mkdir -p %s' % file_path)
    of = open(full_file_name, 'wb+')
    for chunk in content.chunks():
        of.write(chunk)
    of.close()
    Attachment(project_id=project_id, upload_user_id=user_id,
               operate_user_id=user_id,
               file_type=file_type,
               filename=file_name,
               file_path=full_file_name,
               status='new',
               upload_time=datetime.datetime.now()
               ).save()

    return HttpResponse(json.dumps({"ret": True}))


def delete_attachment(request):
    project_id = request.GET.get('project_id')
    file_name = request.GET.get('file_name')
    file_type = request.GET.get('file_type')
    Attachment.objects.filter(project_id=project_id, filename=file_name, file_type=file_type).delete()

    return HttpResponse(json.dumps({"ret": True}))
