# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import json
import datetime
from models import *
from . import select_colums_dict
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from forms import SampleProjectMasterForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from interface import search_result_ini, get_sample_info, common, get_user_cost, check_sample
from interface.common import get_projec_id_by_project_num, get_project_info
# for import django excel
sys.path.append('/usr/local/lib/python2.7/dist-packages')
import django_excel as excel


reload(sys)
sys.setdefaultencoding('utf8')
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
title_map = {'wait_send': u'等待送样', 'send_sample': u'样品送样', 'quality_check': u'样品质检',
             'build_lib': u'样品建库', 'upmachine': u'样品上机', 'downmachine': u'样品下机'}

flow_list = [u'等待送样', u'样品送样', u'样品质检', u'样品建库', u'样品上机', u'样品下机']
# Create your views here.
CODE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def login_required(func):
    """
    Check if already login and search record
    """
    def _decorator(request, *args, **kwargs):
        username = request.session.get('username', '')
        if username:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/lims_app/login/')

    return _decorator


'''
def change_status(project_id, table_name):
    status = SampleProjectMaster.objects.get(id=project_id).status
    if flow_list.index(status) < flow_list.index(table_name):
        SampleProjectMaster.objects.filter(id=project_id).update(status=table_name)
'''


def view_todo(request, table=None):
    project_id = request.GET.get('project_id', '') or 0
    all_proj_info = get_sample_info.get_all_proj_info()
    sample_info = get_sample_info.get_sample_by_project(project_id, name=table)
    '''
    if sample_info:
        change_status(project_id=project_id, table_name=table)
    '''
    select_proj = get_sample_info.get_proj_name_by_id(project_id)
    all_attachment = common.get_attachment(project_id, table)
    all_upload_times = get_sample_info.get_upload_time(project_id=project_id, name=table)

    return (project_id, all_proj_info, sample_info, select_proj, all_attachment, all_upload_times)


def login(request):
    return render(request, 'login.html')


def check_login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        data = {'code': 1, 'msg': ''}
        if not UserInfo.objects.filter(username=username):
            data['msg'] = u'不存在这个用户,请注册!'
        else:
            user = UserInfo.objects.get(username=username)
            if user.password != password:
                data['msg'] = u'密码错误,请重试!'
            elif user.status == 'N':
                data['msg'] = u'该用户未通过验证!'
            else:
                data['msg'] = 'ok'
                data['code'] = 0
                request.session['username'] = username
        return JsonResponse(data)

    return HttpResponseRedirect('/')


def logout(request):
    request.session.flush()
    response = HttpResponseRedirect('/')
    return response


def search(request):
    username = request.session.get('username', '')
    if not username:
        response = HttpResponseRedirect('/')
        return response
    key_word = request.GET.get('q').strip()
    table_header, table_values = search_result_ini.get_search_result(key_word)

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'search_data.html'),
                  {'username': username, 'key_word': key_word, 'table_header': table_header,
                   'table_values': table_values, 'count': len(table_values)})


def operation_log(request):
    username = request.session.get('username', '')
    if not username:
        response = HttpResponseRedirect('/lims_app/login/')
        return response

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'operation_log.html'))


def show_project_master(request):
    if request.method == 'POST':
        all_projects = SampleProjectMaster.objects.all()
        all_projects_list = []
        for each_project in all_projects:
            project_dict = {}
            project_dict['project_number'] = each_project.project_number
            project_dict['create_time'] = each_project.create_time.split(" ")[0]
            project_dict['status'] = each_project.status
            project_dict['comment'] = each_project.comment
            project_dict['cust_user'] = each_project.cust_user
            all_projects_list.append(project_dict)
        return JsonResponse({'data': all_projects_list})


@login_required
def main(request):
    username = request.session.get('username', '')

    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)

    all_projects = SampleProjectMaster.objects.all()
    all_projects_list = []
    for each_project in all_projects:
        project_dict = {}
        project_dict['project_number'] = each_project.project_number
        project_dict['create_time'] = each_project.create_time.split(" ")[0]
        project_dict['status'] = each_project.status
        project_dict['comment'] = each_project.comment
        project_dict['cust_user'] = each_project.cust_user
        all_projects_list.append(project_dict)

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'index.html'),
                      {'username': username, 'all_projects': all_projects_list})


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


'''
view function for onmathlims modules
'''


@login_required
def send_sample(request):
    username = request.session.get('username', '')
    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)
    (project_id, all_proj_info, sample_info, select_proj, all_attachment, all_upload_times) = view_todo(request, table='send_sample')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'receive_sample.html'),
                  {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                   'select_proj': select_proj, 'project_id': project_id,
                   'all_attachment': all_attachment, 'all_upload_times': all_upload_times})


@login_required
def quality_check(request):
    username = request.session.get('username', '')
    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)
    (project_id, all_proj_info, sample_info, select_proj, all_attachment, all_upload_times) = view_todo(request, table='quality_check')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'quality_check.html'),
                  {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                   'select_proj': select_proj, 'project_id': project_id,
                   'all_attachment': all_attachment, 'all_upload_times': all_upload_times})


@login_required
def build_lib(request):
    username = request.session.get('username', '')
    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)
    (project_id, all_proj_info, sample_info, select_proj, all_attachment, all_upload_times) = view_todo(request, table='build_lib')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'build_lib.html'),
                    {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                     'select_proj': select_proj, 'project_id': project_id,
                     'all_attachment': all_attachment, 'all_upload_times': all_upload_times})


@login_required
def upmachine(request):
    username = request.session.get('username', '')
    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)
    (project_id, all_proj_info, sample_info, select_proj, all_attachment, all_upload_times) = view_todo(request, table='upmachine')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'upmachine.html'),
                    {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                     'select_proj': select_proj, 'project_id': project_id,
                     'all_attachment': all_attachment, 'all_upload_times': all_upload_times})


@login_required
def downmachine(request):
    username = request.session.get('username', '')
    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)
    (project_id, all_proj_info, sample_info, select_proj, all_attachment, all_upload_times) = view_todo(request, table='downmachine')

    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'downmachine.html'),
                    {'username': username, 'proj_info': all_proj_info, 'sample_info': sample_info,
                     'select_proj': select_proj, 'project_id': project_id,
                     'all_attachment': all_attachment, 'all_upload_times': all_upload_times})


@login_required
def return_sample(request):
    username = request.session.get('username', '')
    if 'search' in request.GET.keys() or 'q' in request.GET.keys():
        key_word = request.GET.get('q')
        return redirect('/lims_app/search?q=%s' % key_word)

    return_info = get_sample_info.get_return_sample()
    all_upload_times = get_sample_info.get_upload_time(project_id='', name='return_sample')
    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'return_sample.html'),
                  {'username': username, 'return_info': return_info, 'all_upload_times': all_upload_times})


def save_sample_info(request):
    table_name = request.GET.get('table')
    field = request.GET.get('field')
    sample_id = request.POST['name']
    value = request.POST['value']
    if table_name == 'send_sample':
        SendSample.objects.filter(id=sample_id.replace('sample_id_', '')).update(comment=value)
    elif table_name == 'quality_check':
        QualityCheck.objects.filter(id=sample_id.replace('sample_id_', '')).update(comment=value)
    elif table_name == 'build_lib':
        BuildLib.objects.filter(id=sample_id.replace('sample_id_', '')).update(comment=value)
    elif table_name == 'upmachine':
        UpMachine.objects.filter(id=sample_id.replace('sample_id_', '')).update(comment=value)
    elif table_name == 'downmachine':
        DownMachine.objects.filter(id=sample_id.replace('sample_id_', '')).update(comment=value)
    elif table_name == 'return_sample':
        ReturnSample.objects.filter(id=sample_id.replace('sample_id_', '')).update(comment=value)
    elif table_name == 'project_info':
        if field == 'comment':
            SampleProjectMaster.objects.filter(project_number=sample_id).update(comment=value)
        elif field == 'status':
            SampleProjectMaster.objects.filter(project_number=sample_id).update(status=value)
        else:
            return JsonResponse({'msg': 'error'})
    else:
        return JsonResponse({'msg': 'error'})

    return JsonResponse({'msg': 'ok'})


def down_sample_info(request):
    title = {'quality_check': u'质检', 'send_sample': u'送样', 'build_lib': u'建库',
                        'upmachine': u'上机', 'downmachine': u'下机'}

    table_name = request.GET.get('table', '')
    project_number = request.GET.get('project_number', '')
    if table_name and project_number:
        if table_name == 'send_sample':
            query_sets = SendSample.objects.filter(project_number=project_number, status='Y')
            column_names = select_colums_dict.get('send_sample')
        elif table_name == 'quality_check':
            query_sets = QualityCheck.objects.filter(project_number=project_number, status='Y')
            column_names = select_colums_dict.get('quality_check')
        elif table_name == 'build_lib':
            query_sets = BuildLib.objects.filter(project_number=project_number, status='Y')
            column_names = select_colums_dict.get('build_lib')
        elif table_name == 'upmachine':
            query_sets = UpMachine.objects.filter(project_number=project_number, status='Y')
            column_names = select_colums_dict.get('upmachine')
        elif table_name == 'downmachine':
            query_sets = DownMachine.objects.filter(project_number=project_number, status='Y')
            column_names = select_colums_dict.get('downmachine')
        print 'query_sets: ', query_sets
        print 'column_names: ', column_names
        print 'file_name: ', project_number + title[table_name] + u'结果'
        return excel.make_response_from_query_sets(query_sets, column_names, 'xls', file_name=project_number + title[table_name] + u'结果')
    else:
        JsonResponse({'msg': 'error'})


@login_required
def upload_sample_info(request):
    title = {'quality_check': u'质检', 'send_sample': u'送样', 'build_lib': u'建库',
             'upmachine': u'上机', 'downmachine': u'下机', 'return_sample': u'返样'}

    username = request.COOKIES.get('username', '')
    table_name = request.GET['table']
    project_id = ''
    if table_name != 'return_sample':
        project_id = request.GET['project_id']
    if table_name or project_id:
        return render(request,  os.path.join(CODE_ROOT, 'lims_app/templates', 'upload.html'),
                        {'username': username, 'table': table_name, 'table_name': title[table_name], 'project_id': project_id})


def save_sample_row(request):
    request
    return JsonResponse({'msg': 'ok'})


def save_sample_table(request):
    username = request.session.get('username', '')
    json_data = request.POST['sample_table_data']
    json_data = json.loads(json_data)
    project_id = request.POST.get('project_id', '')
    table_name = request.POST['table']

    if table_name == 'return_sample':
        response = check_sample.import_return_sample(json_data)
    elif table_name == 'send_sample':
        response = check_sample.import_send_sample(project_id, json_data, username)
    elif table_name == 'quality_check':
        response = check_sample.import_quality_check(project_id, json_data, username)
    elif table_name == 'build_lib':
        response = check_sample.import_build_lib(project_id, json_data, username)
    elif table_name == 'upmachine':
        response = check_sample.import_upmachine(project_id, json_data, username)
    elif table_name == 'downmachine':
        response = check_sample.import_downmachine(project_id, json_data, username)
    return response


'''
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

    return redirect('/lims_app/send_sample/?project_id=%s' % project_id)
'''


def upload_attachment(request):
    username = request.session.get('username', '')
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
               comment='',
               location='',
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


def save_upload_info(request):
    table = request.GET.get('table')
    field = request.GET.get('field')
    sample_id = request.POST['name']
    value = request.POST['value']
    if table == 'upmachine':
        if field == 'comment':
            Attachment.objects.filter(id=sample_id.replace('sample_id_', '')).update(comment=value)
            return JsonResponse({'msg': 'up-c'})
        elif field == 'location':
            Attachment.objects.filter(id=sample_id.replace('sample_id_', '')).update(location=value)
            return JsonResponse({'msg': 'up-l'})
        else:
            return JsonResponse({'msg': 'error'})
    elif table == 'downmachine':
        if field == 'comment':
            Attachment.objects.filter(id=sample_id.replace('sample_id_', '')).update(comment=vaule)
            return JsonResponse({'msg': 'do-c'})
        elif field == 'location':
            Attachment.objects.filter(id=sample_id.replace('sample_id_', '')).update(location=vaule)
            return JsonResponse({'msg': 'do-l'})
        else:
            return JsonResponse({'msg': 'error'})
    else:
        return JsonResponse({'msg': 'error'})


'''
add user expense page and functions
'''


@login_required
def show_user_detail(request):
    username = request.session.get('username', '')
    cust_user = request.GET.get('user', '')

    billing_total = get_user_cost.get_expense_total(cust_user, 'billing_info')
    receipt_total = get_user_cost.get_expense_total(cust_user, 'receipt_info')
    cost_total = get_user_cost.get_expense_total(cust_user, 'cost_info')
    return render(request, os.path.join(CODE_ROOT, 'lims_app/templates', 'show_user_detail.html'),
                  {'username': username, 'cust_user':cust_user, 'billing_total': billing_total,
                  'receipt_total': receipt_total, 'cost_total': cost_total})


def down_expense_info(request):
    table_name = request.GET.get('table')
    cust_user = request.GET.get('user')
    file_path = get_user_cost.down_expense_table(cust_user, table_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=%s' % os.path.basename(file_path)
            return response

    raise Http404


def show_expense_detail(request):
    cust_user = request.GET.get('user', '')
    table = request.GET.get('table', '')
    page = request.GET.get('page', '')
    limit = request.GET.get('rows', '')
    sidx = request.GET.get('sidx', 'expense')
    sord = request.GET.get('sord', '')
    data = {}
    page, total_pages, count, results = get_user_cost.get_expense_info(cust_user, limit, sidx, sord, page, table)
    data['page'] = page,
    data['total'] = total_pages,
    data['records'] = count
    data['rows'] = []
    for result in results:
        tmp_dict = {}
        tmp_dict['id'] = result[0]
        tmp_dict['cell'] = result[1:len(result)-1]
        data['rows'].append(tmp_dict)

    return JsonResponse(data)


def manage_billing_info(request):
    if request.method == 'POST':
        oper = request.POST['oper']
        if oper == 'del':
            BillingInfo.objects.filter(id=request.POST['id']).delete()
            return HttpResponse({'msg': 'delete'})
        elif oper == 'add':
            project_id = SampleProjectMaster.objects.get(project_number=request.POST['project_number']).id
            new_row = BillingInfo(project_id=project_id,
                                  project_number=request.POST['project_number'],
                                  expense=request.POST['expense'],
                                  billing_number=request.POST['billing_number'],
                                  time=datetime.datetime.now(),
                                  comment=request.POST['comment'])
            new_row.save()
            LogInfo(project_id=project_id,
                    action=u'添加开票信息',
                    time=datetime.datetime.now(),
                    manager=request.session.get('username')).save()
            return HttpResponse({'msg': 'add'})
        else:
            project_id = SampleProjectMaster.objects.get(project_number=request.POST['project_number']).id
            BillingInfo.objects.filter(id=request.POST['id']).update(expense=request.POST['expense'],
                                                                     billing_number=request.POST['billing_number'],
                                                                     time=datetime.datetime.now(),
                                                                     comment=request.POST['comment'])
            LogInfo(project_id=project_id,
                    action=u'修改开票信息',
                    time=datetime.datetime.now(),
                    manager=request.session.get('username')).save()
            return HttpResponse({'msg': 'update'})


def manage_receipt_info(request):
    if request.method == 'POST':
        oper = request.POST['oper']
        if oper == 'del':
            ReceiptInfo.objects.filter(id=request.POST['id']).delete()
            return HttpResponse({'msg': 'delete'})
        elif oper == 'add':
            project_id = SampleProjectMaster.objects.get(project_number=request.POST['project_number']).id
            new_row = ReceiptInfo(project_id=project_id,
                                  project_number=request.POST['project_number'],
                                  expense=request.POST['expense'],
                                  time=datetime.datetime.now(),
                                  comment=request.POST['comment'])
            new_row.save()
            LogInfo(project_id=project_id,
                    action=u'增加收票信息',
                    time=datetime.datetime.now(),
                    manager=request.session.get('username')).save()
            return HttpResponse({'msg': 'add'})
        else:
            project_id = SampleProjectMaster.objects.get(project_number=request.POST['project_number']).id
            ReceiptInfo.objects.filter(id=request.POST['id']).update(expense=request.POST['expense'],
                                                                     time=datetime.datetime.now(),
                                                                     comment=request.POST['comment'])
            LogInfo(project_id=project_id,
                    action=u'修改收票信息',
                    time=datetime.datetime.now(),
                    manager=request.session.get('username')).save()
            return HttpResponse({'msg': 'update'})


def manage_cost_info(request):
    if request.method == 'POST':
        oper = request.POST['oper']
        if oper == 'del':
            CostInfo.objects.filter(id=request.POST['id']).delete()
            return HttpResponse({'msg': 'delete'})
        elif oper == 'add':
            project_id = SampleProjectMaster.objects.get(project_number=request.POST['project_number']).id
            new_row = CostInfo(project_id=project_id,
                               project_number=request.POST['project_number'],
                               expense=request.POST['expense'],
                               sample_number=request.POST['sample_number'],
                               unit_cost=request.POST['unit_cost'],
                               time=datetime.datetime.now(),
                               comment=request.POST['comment'])
            new_row.save()
            LogInfo(project_id=project_id,
                    action=u'新增成本信息',
                    time=datetime.datetime.now(),
                    manager=request.session.get('username')).save()
            return HttpResponse({'msg': 'add'})
        else:
            project_id = SampleProjectMaster.objects.get(project_number=request.POST['project_number']).id
            CostInfo.objects.filter(id=request.POST['id']).update(expense=request.POST['expense'],
                                                                  sample_number=request.POST['sample_number'],
                                                                  unit_cost=request.POST['unit_cost'],
                                                                  time=datetime.datetime.now(),
                                                                  comment=request.POST['comment'])
            LogInfo(project_id=project_id,
                    action=u'修改成本信息',
                    time=datetime.datetime.now(),
                    manager=request.session.get('username')).save()
            return HttpResponse({'msg': 'update'})


def recover_data(request):
    username = request.session.get('username', '')
    table = request.GET.get('table', '')
    project_id = request.GET.get('project_id', '')
    upload_time = request.GET.get('upload_time', '')
    # action = request.GET.get('action', '')

    response = check_sample.recover_data(table, upload_time, username, project_id)
    return response


def show_project_detail(request):
    project_number = request.GET.get('project_number', '')
    user = request.GET.get('user', '')
    project_id = get_projec_id_by_project_num(project_number)
    info = get_project_info(project_id)
    project_info = get_sample_info.get_project_summary(project_id)
    exp_dict = get_user_cost.check_bill(user, project_id)

    return render(request, 'project_detail.html', {'info': info,
                                                   'exp_dict': exp_dict,
                                                   'project_number': project_number,
                                                   'project_info': project_info})


def download_summary_info(request):
    project_number = request.GET.get('project_number', '')
    project_id = get_projec_id_by_project_num(project_number)
    file_path = get_sample_info.download_summary_table(project_id)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=%s' % os.path.basename(file_path)
            return response

    raise Http404
