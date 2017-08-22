# coding:utf-8

import datetime
from django.http import JsonResponse
from django.db import connection
from lims_app.models import SendSample, QualityCheck, BuildLib, UpMachine, DownMachine, SampleProjectMaster


def get_db_data(cmd, get_all=True):
    cursor = connection.cursor()
    cursor.execute(cmd)
    if get_all:
        result = cursor.fetchall()
    else:
        result = cursor.fetchone()

    return result


def get_sample_type(project_id):
    cmd = "select * from sample_type where project_id='%s'" % (project_id)
    result = get_db_data(cmd, get_all=False)
    dna_type = result[2:8]

    if 'Y' in dna_type:
        return 'D'
    else:
        return 'R'


def check_sample(table, project_id, new_ids):
    flow_list = ['send_sample', 'quality_check', 'build_lib', 'upmachine', 'downmachine']
    before_table = flow_list[flow_list.index(table)-1]

    cmd = "select om_id from %s where project_id='%s'" % (before_table, project_id)
    results = get_db_data(cmd)
    results = [result[0] for result in results]

    if not set(new_ids).issubset(set(results)):
        return False
    else:
        return True


def split_data(table, project_id, json_data):
    cmd = "select om_id from %s where project_id='%s'" % (table, project_id)
    results = get_db_data(cmd)
    om_ids = []
    for row_dict in json_data:
        om_ids.append(row_dict['om_id'])
    old_id_set = set([result[0] for result in results])
    new_id_set = set(om_ids)
    insert_id = list(new_id_set.difference(old_id_set))
    insert_data = []
    update_data = []
    for row_dict in json_data:
        if row_dict['om_id'] in insert_id:
            insert_data.append(row_dict)
        else:
            update_data.append(row_dict)

    return insert_data, update_data


def import_data(table, project_id, json_data):
    project_number = SampleProjectMaster.objects.get(id=project_id).project_number
    if table == 'send_sample':
        if json_data[0].get('om_id'):
            # insert_data, update_data = split_data(table, project_id, json_data)
            for row_dict in json_data:
                SendSample.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
                p = SendSample(project_number=project_number,
                               project_id=project_id,
                               sample_name=row_dict['sample_name'],
                               om_id=row_dict['om_id'],
                               species=row_dict['species'],
                               express_number=row_dict['express_number'],
                               product_num=row_dict['product_num'],
                               create_time=row_dict['time'],
                               comment=row_dict['comment'],
                               upload_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                               status='Y')
                p.save()
            return JsonResponse({'msg': u'更新成功!'})
        else:
            sample_type = get_sample_type(project_id)
            prefix = ''.join(['P', str(project_id), sample_type, datetime.datetime.now().date().strftime("%y%m"),'N'])
            cmd = "select om_id from %s where project_id='%s'" % (table, project_id)
            results = get_db_data(cmd)
            if results:
                max_number = max([int(result[0].split('N')[1]) for result in results])+1
            else:
                max_number = 1

            for i, row_dict in enumerate(json_data):
                om_id = ''.join([prefix, str(i+max_number)])
                p = SendSample(project_number=project_number,
                               project_id=project_id,
                               sample_name=row_dict['sample_name'],
                               om_id=om_id,
                               species=row_dict['species'],
                               express_number=row_dict['express_number'],
                               product_num=row_dict['product_num'],
                               create_time=row_dict['time'],
                               comment=row_dict['comment'],
                               upload_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                               status='Y')
                p.save()
            return JsonResponse({'msg': u'导入成功!'})

    elif table == 'quality_check':
        om_ids = [row_dict['om_id'] for row_dict in json_data]
        if check_sample(table, project_id, om_ids):
            insert_data, update_data = split_data(table, project_id, json_data)
            if update_data:
                for row_dict in update_data:
                    QualityCheck.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
            for row_dict in json_data:
                p = QualityCheck(project_id=project_id,
                                 project_number=project_number,
                                 sample_name=row_dict['sample_name'],
                                 om_id=row_dict['om_id'],
                                 sample_id=row_dict['sample_id'],
                                 concentration=row_dict['concentration'],
                                 volume=row_dict['volume'],
                                 rin=row_dict['rin'],
                                 results=row_dict['results'],
                                 create_time=row_dict['time'],
                                 comment=row_dict['comment'],
                                 upload_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                                 status='Y')
                p.save()
            return JsonResponse({'msg': u'导入成功!'})
        else:
            return JsonResponse({'msg': u'数据中存在非法om_id!'})
    elif table == 'build_lib':
        om_ids = [row_dict['om_id'] for row_dict in json_data]
        if check_sample(table, project_id, om_ids):
            insert_data, update_data = split_data(table, project_id, json_data)
            if update_data:
                for row_dict in update_data:
                    BuildLib.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
            for row_dict in json_data:
                p = BuildLib(project_id=project_id,
                             project_number=project_number,
                             sample_name=row_dict['sample_name'],
                             om_id=row_dict['om_id'],
                             sample_id=row_dict['sample_id'],
                             lib_id=row_dict['lib_id'],
                             create_time=row_dict['time'],
                             comment=row_dict['comment'],
                             upload_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                             status='Y')
                p.save()
            return JsonResponse({'msg': u'导入成功!'})
        else:
            return JsonResponse({'msg': u'数据中存在非法om_id!'})
    elif table == 'upmachine':
        om_ids = [row_dict['om_id'] for row_dict in json_data]
        if check_sample(table, project_id, om_ids):
            insert_data, update_data = split_data(table, project_id, json_data)
            if update_data:
                for row_dict in update_data:
                    UpMachine.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
            for row_dict in json_data:
                p = UpMachine(project_id=project_id,
                              project_number=project_number,
                              sample_name=row_dict['sample_name'],
                              om_id=row_dict['om_id'],
                              sample_id=row_dict['sample_id'],
                              upmachinetype=row_dict['upmachinetype'],
                              mode=row_dict['mode'],
                              data_count=row_dict['data_count'],
                              create_time=row_dict['time'],
                              comment=row_dict['comment'],
                              upload_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                              status='Y')
                p.save()
            return JsonResponse({'msg': u'导入成功!'})
        else:
            return JsonResponse({'msg': u'数据中存在非法om_id!'})
    elif table == 'downmachine':
        om_ids = [row_dict['om_id'] for row_dict in json_data]
        if check_sample(table, project_id, om_ids):
            insert_data, update_data = split_data(table, project_id, json_data)
            if update_data:
                for row_dict in update_data:
                    DownMachine.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
            for row_dict in json_data:
                p = DownMachine(project_id=project_id,
                                project_number=project_number,
                                sample_name=row_dict['sample_name'],
                                om_id=row_dict['om_id'],
                                sample_id=row_dict['sample_id'],
                                q20=row_dict['q20'],
                                q30=row_dict['q30'],
                                data_count=row_dict['data_count'],
                                create_time=row_dict['time'],
                                comment=row_dict['comment'],
                                upload_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                                status='Y')
                p.save()
            return JsonResponse({'msg': u'导入成功!'})
        else:
            return JsonResponse({'msg': u'数据中存在非法om_id!'})
    else:
        return JsonResponse({'msg': 'error!'})


def recover_data(project_id, table, upload_time, action):
    '''
    recover data at most three times
    upload_time format: "%Y-%m-%d %H:%M"
    '''

    # upload_time = datetime.datetime.strptime(upload_time, "%Y-%m-%d %H:%M")
    if table == 'send_sample':
        if action == 'recover':
            SendSample.objects.filter(project_id=project_id,
                                      upload_time=upload_time,
                                      status='N').update(status='Y')
            return JsonResponse({'msg': u'重置成功!'})
        else:
            SendSample.objects.filter(project_id=project_id,
                                      upload_time=upload_time,
                                      status='Y').update(status='N')
            return JsonResponse({'msg': u'删除成功!'})
    elif table == 'quality_check':
        if action == 'recover':
            QualityCheck.objects.filter(project_id=project_id,
                                        upload_time=upload_time,
                                        status='N').update(status='Y')
            return JsonResponse({'msg': u'重置成功!'})
        else:
            QualityCheck.objects.filter(project_id=project_id,
                                        upload_time=upload_time,
                                        status='Y').update(status='N')
            return JsonResponse({'msg': u'删除成功!'})
    elif table == 'build_lib':
        if action == 'recover':
            BuildLib.objects.filter(project_id=project_id,
                                    upload_time=upload_time,
                                    status='N').update(status='Y')
            return JsonResponse({'msg': u'重置成功!'})
        else:
            BuildLib.objects.filter(project_id=project_id,
                                    upload_time=upload_time,
                                    status='Y').update(status='N')
            return JsonResponse({'msg': u'删除成功!'})
    elif table == 'upmachine':
        if action == 'recover':
            UpMachine.objects.filter(project_id=project_id,
                                     upload_time=upload_time,
                                     status='N').update(status='Y')
            return JsonResponse({'msg': u'重置成功!'})
        else:
            UpMachine.objects.filter(project_id=project_id,
                                     upload_time=upload_time,
                                     status='Y').update(status='N')
            return JsonResponse({'msg': u'删除成功!'})
    elif table == 'downmachine':
        if action == 'recover':
            DownMachine.objects.filter(project_id=project_id,
                                       upload_time=upload_time,
                                       status='N').update(status='Y')
            return JsonResponse({'msg': u'重置成功!'})
        else:
            DownMachine.objects.filter(project_id=project_id,
                                       upload_time=upload_time,
                                       status='Y').update(status='N')
            return JsonResponse({'msg': u'删除成功!'})
    else:
        return JsonResponse({'msg': 'error!'})
