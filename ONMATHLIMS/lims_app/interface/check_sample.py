# coding:utf-8

import datetime
from django.http import JsonResponse
from django.db import connection
from lims_app.models import SendSample, QualityCheck, BuildLib, UpMachine, DownMachine, SampleProjectMaster, ReturnSample, LogInfo


def get_db_data(cmd, get_all=True):
    '''
    get database data
    '''
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


def get_repeat_sample(json_data):
    sample_name = [row_dict['sample_name'] for row_dict in json_data]
    repeat_sample_name = [sample for sample in sample_name if sample_name.count(sample) > 1]
    repeat_sample_name = list(set(repeat_sample_name))
    repeat_dict = {sample: sample_name.count(sample) for sample in repeat_sample_name}
    return repeat_dict


def map_omid(table, project_id):
    flow_list = ['send_sample', 'quality_check', 'build_lib', 'upmachine', 'downmachine', 'return_sample']
    before_table = table
    # 如果没有找到最近的表就会一直往上取表
    while True:
        before_table = flow_list[flow_list.index(before_table)-1]
        cmd = "select sample_id, om_id from %s where project_id='%s' and status='Y'" % (before_table, project_id)
        results = get_db_data(cmd)
        if results:
            break

    sample_id = [result[0] for result in results]
    map_dict = {k: '' for k in sample_id}
    for sample_id, om_id in results:
        map_dict[sample_id] = om_id

    return map_dict

    '''
    if before_table == 'send_sample':
        cmd = "select sample_name, om_id from send_sample where project_id='%s' and status='Y'" % (project_id)
        results = get_db_data(cmd)
        sample_name = [result[0] for result in results]
        repeat_sample_name = [sample for sample in sample_name if sample_name.count(sample) > 1]
        repeat_sample_name = list(set(repeat_sample_name))
        norepeat_sample_name = [sample for sample in sample_name if sample_name.count(sample) == 1]
        map_dict = {k: [] for k in repeat_sample_name}
        map_dict.update({k: '' for k in norepeat_sample_name})
        for sample_name, om_id in results:
            if sample_name in norepeat_sample_name:
                map_dict[sample_name] = om_id
            else:
                map_dict[sample_name].append(om_id)
        return map_dict
    else:
        cmd = "select sample_id, om_id from %s where project_id='%s' and status='Y'" % (before_table, project_id)
        results = get_db_data(cmd)
        sample_id = [result[0] for result in results]
        map_dict = {k: [] for k in sample_id}
        for sample_id, om_id in results:
            map_dict[sample_id] = om_id

        return map_dict
    '''


def check_sample(table, project_id, new_ids):
    '''
    check om id whether in before table
    '''
    flow_list = ['send_sample', 'quality_check', 'build_lib', 'upmachine', 'downmachine']
    before_table = table

    while True:
        before_table = flow_list[flow_list.index(before_table)-1]
        cmd = "select om_id from %s where project_id='%s' and status='Y'" % (before_table, project_id)
        results = get_db_data(cmd)
        if results:
            break

    results = [result[0] for result in results]
    if not set(new_ids).issubset(set(results)):
        return False
    else:
        return True


def split_data(table, project_id, json_data):
    cmd = "select om_id from %s where project_id='%s' and status='Y'" % (table, project_id)
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


def check_omid(table, project_id, om_ids):
    '''
    check om id whether subset before upload
    '''
    cmd = "select om_id from %s where project_id='%s' and status='Y'" % (table, project_id)
    results = get_db_data(cmd)
    results = [result[0] for result in results]
    for om_id in om_ids:
        if om_id not in results:
            return 'error'
    return 'ok'


def import_data(table, project_id, json_data, username):
    project_number = SampleProjectMaster.objects.get(id=project_id).project_number
    if table == 'send_sample':
        if json_data[0].get('om_id'):
            om_ids = [row_dict['om_id'] for row_dict in json_data]
            if check_omid(table, project_id, om_ids) == 'error':
                return JsonResponse({'msg': u'存在没有的OMID!'})
            # insert_data, update_data = split_data(table, project_id, json_data)
            try:
                upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                for row_dict in json_data:
                    SendSample.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
                    p = SendSample(project_number=project_number,
                                   project_id=project_id,
                                   sample_name=row_dict['sample_name'],
                                   om_id=row_dict['om_id'],
                                   sample_id=row_dict['sample_id'],
                                   species=row_dict['species'],
                                   express_number=row_dict['express_number'],
                                   product_num=row_dict['product_num'],
                                   create_time=row_dict['time'],
                                   comment=row_dict['comment'],
                                   upload_time=upload_time,
                                   status='Y')
                    p.save()
            except:
                SendSample.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                return JsonResponse({'msg': u'数据格式错误(时间格式)!'})

            LogInfo(project_id=project_id, action='更新了样品信息表', time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'更新成功!'})
        else:
            sample_type = get_sample_type(project_id)
            prefix = ''.join(['P', str(project_id), sample_type, datetime.datetime.now().date().strftime("%y%m"),'N'])
            cmd = "select om_id from %s where project_id='%s' and status='Y'" % (table, project_id)
            results = get_db_data(cmd)
            if results:
                max_number = max([int(result[0].split('N')[1]) for result in results])
            else:
                max_number = 0

            om_num = 0
            om_num += max_number
            upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            for i, row_dict in enumerate(json_data):
                '''
                if int(row_dict['product_num']) != 1:
                    for j in range(int(row_dict['product_num'])):
                        om_num += 1
                        om_id = ''.join([prefix, str(om_num)])
                        try:
                            p = SendSample(project_number=project_number,
                                           project_id=project_id,
                                           sample_name=row_dict['sample_name'],
                                           om_id=om_id,
                                           species=row_dict['species'],
                                           express_number=row_dict['express_number'],
                                           product_num=1,
                                           create_time=row_dict['time'],
                                           comment=row_dict['comment'],
                                           upload_time=upload_time,
                                           status='Y')
                            p.save()
                        except:
                            SendSample.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                            return JsonResponse({'msg': u'数据格式错误(时间格式)!'})
                else:
                '''
                om_num += 1
                om_id = ''.join([prefix, str(om_num)])
                try:
                    p = SendSample(project_number=project_number,
                                   project_id=project_id,
                                   sample_name=row_dict['sample_name'],
                                   om_id=om_id,
                                   sample_id=row_dict['sample_id'],
                                   species=row_dict['species'],
                                   express_number=row_dict['express_number'],
                                   product_num=row_dict['product_num'],
                                   create_time=row_dict['time'],
                                   comment=row_dict['comment'],
                                   upload_time=upload_time,
                                   status='Y')
                    p.save()
                except:
                    SendSample.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'数据格式错误(时间格式)!'})
            LogInfo(project_id=project_id, action='导入了样品信息表', time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'导入成功!'})

    elif table == 'quality_check':
        if json_data[0].get('om_id'):
            om_ids = [row_dict['om_id'] for row_dict in json_data]
            if check_sample(table, project_id, om_ids):
                insert_data, update_data = split_data(table, project_id, json_data)
                if update_data:
                    for row_dict in update_data:
                        QualityCheck.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
                upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                for row_dict in json_data:
                    try:
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
                                         upload_time=upload_time,
                                         status='Y')
                        p.save()
                    except:
                        QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                        return JsonResponse({'msg': u'数据格式错误(时间格式)!'})

                LogInfo(project_id=project_id, action='导入了质检信息表', time=datetime.datetime.now(), manager=username).save()
                return JsonResponse({'msg': u'导入成功!'})
            else:
                LogInfo(project_id=project_id, action='导入了样品信息表失败， 数据中存在非法om_id!',
                        time=datetime.datetime.now(), manager=username).save()
                return JsonResponse({'msg': u'数据中存在非法om_id!'})
        else:
            map_dict = map_omid('quality_check', project_id)
            upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            for i, row_dict in enumerate(json_data):
                try:
                    p = QualityCheck(project_id=project_id,
                                     project_number=project_number,
                                     sample_name=row_dict['sample_name'],
                                     om_id=map_dict[row_dict['sample_id']],
                                     sample_id=row_dict['sample_id'],
                                     concentration=row_dict['concentration'],
                                     volume=row_dict['volume'],
                                     rin=row_dict['rin'],
                                     results=row_dict['results'],
                                     create_time=row_dict['time'],
                                     comment=row_dict['comment'],
                                     upload_time=upload_time,
                                     status='Y')
                    p.save()
                except KeyError:
                    QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'没有找到{0}!'.format(row_dict['sample_id'])})
                except ValueError:
                    QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'数据格式错误(时间格式)!'})

            LogInfo(project_id=project_id, action='导入了质检信息表', time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'导入成功!'})
    elif table == 'build_lib':
        if json_data[0].get('om_id'):
            om_ids = [row_dict['om_id'] for row_dict in json_data]
            if check_sample(table, project_id, om_ids):
                insert_data, update_data = split_data(table, project_id, json_data)
                if update_data:
                    for row_dict in update_data:
                        BuildLib.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
                    upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                try:
                    for row_dict in json_data:
                        p = BuildLib(project_id=project_id,
                                     project_number=project_number,
                                     sample_name=row_dict['sample_name'],
                                     om_id=row_dict['om_id'],
                                     sample_id=row_dict['sample_id'],
                                     lib_id=row_dict['lib_id'],
                                     create_time=row_dict['time'],
                                     comment=row_dict['comment'],
                                     upload_time=upload_time,
                                     status='Y')
                        p.save()
                except:
                    BuildLib.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'数据格式错误(时间格式)!'})

                LogInfo(project_id=project_id, action='导入了建库信息表', time=datetime.datetime.now(), manager=username).save()
                return JsonResponse({'msg': u'导入成功!'})
            else:
                LogInfo(project_id=project_id, action='导入建库信息表失败， 数据中存在非法om_id!',
                        time=datetime.datetime.now(), manager=username).save()
                return JsonResponse({'msg': u'数据中存在非法om_id!'})
        else:
            map_dict = map_omid('build_lib', project_id)
            upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            for i, row_dict in enumerate(json_data):
                try:
                    p = BuildLib(project_id=project_id,
                                 project_number=project_number,
                                 sample_name=row_dict['sample_name'],
                                 om_id=map_dict[row_dict['sample_id']],
                                 sample_id=row_dict['sample_id'],
                                 lib_id=row_dict['lib_id'],
                                 create_time=row_dict['time'],
                                 comment=row_dict['comment'],
                                 upload_time=upload_time,
                                 status='Y')
                    p.save()
                except KeyError:
                    QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'没有找到{0}!'.format(row_dict['sample_id'])})
                except ValueError:
                    QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'数据格式错误(时间格式)!'})
            LogInfo(project_id=project_id, action='导入了建库信息表', time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'导入成功!'})
    elif table == 'upmachine':
        if json_data[0].get('om_id'):
            om_ids = [row_dict['om_id'] for row_dict in json_data]
            if check_sample(table, project_id, om_ids):
                insert_data, update_data = split_data(table, project_id, json_data)
                if update_data:
                    for row_dict in update_data:
                        UpMachine.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
                upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                try:
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
                                      upload_time=upload_time,
                                      status='Y')
                        p.save()
                except:
                    UpMachine.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'数据格式错误(时间格式)!'})

                    LogInfo(project_id=project_id, action='导入了上机信息表', time=datetime.datetime.now(), manager=username).save()
                    return JsonResponse({'msg': u'导入成功!'})
            else:
                LogInfo(project_id=project_id, action='导入上机信息表失败， 数据中存在非法om_id!',
                        time=datetime.datetime.now(), manager=username).save()
                return JsonResponse({'msg': u'数据中存在非法om_id!'})
        else:
            map_dict = map_omid('upmachine', project_id)
            upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            for i, row_dict in enumerate(json_data):
                try:
                    p = UpMachine(project_id=project_id,
                                  project_number=project_number,
                                  sample_name=row_dict['sample_name'],
                                  om_id=map_dict[row_dict['sample_id']],
                                  sample_id=row_dict['sample_id'],
                                  upmachinetype=row_dict['upmachinetype'],
                                  mode=row_dict['mode'],
                                  data_count=row_dict['data_count'],
                                  create_time=row_dict['time'],
                                  comment=row_dict['comment'],
                                  upload_time=upload_time,
                                  status='Y')
                    p.save()
                except KeyError:
                    QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'没有找到{0}!'.format(row_dict['sample_id'])})
                except ValueError:
                    QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'数据格式错误(时间格式)!'})
            LogInfo(project_id=project_id, action='导入了上机信息表', time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'导入成功!'})
    elif table == 'downmachine':
        if json_data[0].get('om_id'):
            om_ids = [row_dict['om_id'] for row_dict in json_data]
            if check_sample(table, project_id, om_ids):
                insert_data, update_data = split_data(table, project_id, json_data)
                if update_data:
                    for row_dict in update_data:
                        DownMachine.objects.filter(om_id=row_dict['om_id'], status='Y').update(status='N')
                upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                try:
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
                                        upload_time=upload_time,
                                        status='Y')
                        p.save()
                except:
                    DownMachine.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'数据格式错误(时间格式)!'})

                LogInfo(project_id=project_id, action='导入了下机信息表', time=datetime.datetime.now(), manager=username).save()
                return JsonResponse({'msg': u'导入成功!'})
            else:
                LogInfo(project_id=project_id, action='导入下机信息表失败， 数据中存在非法om_id!',
                        time=datetime.datetime.now(), manager=username).save()
                return JsonResponse({'msg': u'数据中存在非法om_id!'})
        else:
            map_dict = map_omid('downmachine', project_id)
            upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            for i, row_dict in enumerate(json_data):
                try:
                    p = DownMachine(project_id=project_id,
                                    project_number=project_number,
                                    sample_name=row_dict['sample_name'],
                                    om_id=map_dict[row_dict['sample_id']],
                                    sample_id=row_dict['sample_id'],
                                    q20=row_dict['q20'],
                                    q30=row_dict['q30'],
                                    data_count=row_dict['data_count'],
                                    create_time=row_dict['time'],
                                    comment=row_dict['comment'],
                                    upload_time=upload_time,
                                    status='Y')
                    p.save()
                except KeyError:
                    QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'没有找到{0}!'.format(row_dict['sample_id'])})
                except ValueError:
                    QualityCheck.objects.filter(project_id=project_id, upload_time=upload_time).delete()
                    return JsonResponse({'msg': u'数据格式错误(时间格式)!'})
            LogInfo(project_id=project_id, action='导入了下机信息表', time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'导入成功!'})
    else:
        return JsonResponse({'msg': 'error!'})


def recover_data(table, upload_time, username, project_id=''):
    '''
    recover data at most three times
    upload_time format: "%Y-%m-%d %H:%M"
    '''

    # upload_time = datetime.datetime.strptime(upload_time, "%Y-%m-%d %H:%M")
    if table == 'send_sample':
        '''
        if action == 'recover':
            SendSample.objects.filter(project_id=project_id,
                                      upload_time=upload_time,
                                      status='N').update(status='Y')
            LogInfo(project_id=project_id, action='重置了样品信息表到上传日期%s' % upload_time,
                    time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'重置成功!'})
        '''
        SendSample.objects.filter(project_id=project_id,
                                  upload_time=upload_time,
                                  status='Y').update(status='N')
        LogInfo(project_id=project_id, action='重置了样品信息表到上传日期%s' % upload_time,
                time=datetime.datetime.now(), manager=username).save()
        return JsonResponse({'msg': u'删除成功!'})
    elif table == 'quality_check':
        '''
        if action == 'recover':
            QualityCheck.objects.filter(project_id=project_id,
                                        upload_time=upload_time,
                                        status='N').update(status='Y')
            LogInfo(project_id=project_id, action='重置了质检信息表到上传日期%s' % upload_time,
                    time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'重置成功!'})
        '''
        QualityCheck.objects.filter(project_id=project_id,
                                    upload_time=upload_time,
                                    status='Y').update(status='N')
        LogInfo(project_id=project_id, action='重置了质检信息表到上传日期%s' % upload_time,
                time=datetime.datetime.now(), manager=username).save()
        return JsonResponse({'msg': u'删除成功!'})
    elif table == 'build_lib':
        '''
        if action == 'recover':
            BuildLib.objects.filter(project_id=project_id,
                                    upload_time=upload_time,
                                    status='N').update(status='Y')
            LogInfo(project_id=project_id, action='重置了建库信息表到上传日期%s' % upload_time,
                    time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'重置成功!'})
        '''
        BuildLib.objects.filter(project_id=project_id,
                                upload_time=upload_time,
                                status='Y').update(status='N')
        LogInfo(project_id=project_id, action='重置了建库信息表到上传日期%s' % upload_time,
                time=datetime.datetime.now(), manager=username).save()
        return JsonResponse({'msg': u'删除成功!'})
    elif table == 'upmachine':
        '''
        if action == 'recover':
            UpMachine.objects.filter(project_id=project_id,
                                     upload_time=upload_time,
                                     status='N').update(status='Y')
            LogInfo(project_id=project_id, action='重置了上机信息表到上传日期%s' % upload_time,
                    time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'重置成功!'})
        '''
        UpMachine.objects.filter(project_id=project_id,
                                 upload_time=upload_time,
                                 status='Y').update(status='N')
        LogInfo(project_id=project_id, action='重置了上机信息表到上传日期%s' % upload_time,
                time=datetime.datetime.now(), manager=username).save()
        return JsonResponse({'msg': u'删除成功!'})
    elif table == 'downmachine':
        '''
        if action == 'recover':
            DownMachine.objects.filter(project_id=project_id,
                                       upload_time=upload_time,
                                       status='N').update(status='Y')
            LogInfo(project_id=project_id, action='重置了下机信息表到上传日期%s' % upload_time,
                    time=datetime.datetime.now(), manager=username).save()
            return JsonResponse({'msg': u'重置成功!'})
        '''
        DownMachine.objects.filter(project_id=project_id,
                                   upload_time=upload_time,
                                   status='Y').update(status='N')
        LogInfo(project_id=project_id, action='重置了样品下机表到上传日期%s' % upload_time,
                time=datetime.datetime.now(), manager=username).save()
        return JsonResponse({'msg': u'删除成功!'})
    elif table == 'return_sample':
        '''
        if action == 'recover':
            ReturnSample.objects.filter(upload_time=upload_time,
                                        status='N').update(status='Y')
            # get_location()
            return JsonResponse({'msg': u'重置成功!'})
        '''
        ReturnSample.objects.filter(upload_time=upload_time,
                                    status='Y').update(status='N')
        # get_location()
        return JsonResponse({'msg': u'删除成功!'})
    else:
        return JsonResponse({'msg': 'error!'})


def split_return_sample(json_data):
    cmd = "select om_id from return_sample"
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


def get_location():
    cmd = "select sample_id,location from return_sample where status = 'Y'"
    results = get_db_data(cmd)
    for sample_id, location in results:
        QualityCheck.objects.filter(sample_id=sample_id, status='Y').update(location=location)
        BuildLib.objects.filter(sample_id=sample_id, status='Y').update(location=location)
        UpMachine.objects.filter(sample_id=sample_id, status='Y').update(location=location)
        DownMachine.objects.filter(sample_id=sample_id, status='Y').update(location=location)


def import_return_sample(json_data):
    cmd = "select sample_id from return_sample where status = 'Y'"
    results = get_db_data(cmd)
    sample_ids = [row_dict['sample_id'] for row_dict in json_data]
    old_id_set = set([result[0] for result in results])
    new_id_set = set(sample_ids)
    insert_id = list(new_id_set.difference(old_id_set))

    for row_dict in json_data:
        if row_dict['sample_id'] not in insert_id:
            ReturnSample.objects.filter(sample_id=row_dict['sample_id']).update(status='N')

        p = ReturnSample(sample_name=row_dict['sample_name'],
                         # om_id=map_dict[row_dict['sample_id']],
                         sample_id=row_dict['sample_id'],
                         location=row_dict['location'],
                         time=row_dict['time'],
                         upload_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                         comment=row_dict['comment'],
                         status='Y')
        p.save()

    get_location()
    return JsonResponse({'msg': u'导入成功!'})
