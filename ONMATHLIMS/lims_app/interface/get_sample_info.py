# coding: utf8
from django.db import connection

cmd_dict = {'receive_sample': """select *
          from send_sample ss inner join sample_project_master m on m.id=ss.project_id""",
            'quality_check': """select d.id, d.sample_id, d.sample_name,
          d.rin, d.concentration, d.volume, d.qualitycheck_results, qualitycheck_time, qualitycheck_comment
          from sample_info_detail d inner join sample_project_master m on m.id=d.project_id""",
            'build_lib': """select d.id, d.sample_id, d.sample_name,
          d.lib_id, d.lib_time, d.lib_comment
          from sample_info_detail d inner join sample_project_master m on m.id=d.project_id""",
            'upmachine': """select d.id, d.sample_id, d.sample_name,
            d.upmachine_type, d.upmachine_mode, d.upmachine_num, d.upmachine_time, d.upmachine_comment
          from sample_info_detail d inner join sample_project_master m on m.id=d.project_id""",
            'downmachine': """select d.id, d.sample_id, d.sample_name,
          d.downmachine_num, d.q20, d.q30, d.downmachine_time, d.downmachine_comment
          from sample_info_detail d inner join sample_project_master m on m.id=d.project_id"""}


def get_proj_name_by_id(project_id):
    cmd = "SELECT project_number FROM sample_project_master where id='%s'" % project_id
    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchone()

    return result[0] if result else u"请选择项目"


def get_all_proj_info():
    cmd = "select id, project_number from sample_project_master"
    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()

    return result


def get_sample_by_project(project_id, name):
    """
    :param project_id:
    :return:
    where project_id='%s'
    """
    cmd = "select * from %s where project_id='%s' and status='Y'" % (name, project_id)

    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()

    return result


def get_user_id_by_name(username):
    cmd = "select id from user_info where username='%s'" % username
    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchone()

    return result[0] if result else 0


def get_upload_time(project_id, name):
    if name == 'return_sample':
        cmd = "select distinct upload_time,status from %s where status='Y' order by upload_time desc" % (name)
    else:
        cmd = "select distinct upload_time,status from %s where project_id='%s' and status='Y' order by upload_time desc" % (name, project_id)
    cursor = connection.cursor()
    cursor.execute(cmd)
    results = cursor.fetchall()

    return results


def get_return_sample():
    cmd = "select * from return_sample where status='Y'"

    cursor = connection.cursor()
    cursor.execute(cmd)
    results = cursor.fetchall()

    return results


def get_project_summary(project_id):
    cmd = '''
          select ss.sample_name,ss.sample_id,
          ss.om_id,qc.results,um.data_count,
          dm.data_count,ss.location,um.location from
          send_sample ss inner join quality_check qc on
          ss.sample_id=qc.sample_id inner join upmachine um on
          qc.sample_id=um.sample_id inner join downmachine dm on
          um.sample_id=dm.sample_id
          where ss.project_id='%s';
    ''' % (project_id)
    cursor = connection.cursor()
    cursor.execute(cmd)
    results = cursor.fetchall()
    '''
    if not results:
        cmd =
        select ss.sample_name,ss.sample_id,
        ss.om_id,qc.results,um.data_count,
        dm.data_count,um.location,ss.location from
        send_sample ss inner join quality_check qc on
        ss.sample_id=qc.sample_id inner join upmachine um on
        qc.sample_id=um.sample_id inner join downmachine dm on
        um.sample_id=dm.sample_id where ss.project_id='%s';
         % (project_id)
        cursor = connection.cursor()
        cursor.execute(cmd)
        results = cursor.fetchall()
    '''
    return results
