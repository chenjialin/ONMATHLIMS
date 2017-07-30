# coding: utf8
from django.db import connection

cmd_dict = {'receive_sample': """select d.id, d.sample_name,
          d.express_number, d.product_num, d.sendsample_time, d.sendsample_comment
          from sample_info_detail d inner join sample_project_master m on m.id=d.project_id""",
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


def get_sample_by_project(project_id, name='receive_sample'):
    """
    :param project_id:
    :return:
    where project_id='%s'
    """
    cmd = cmd_dict[name] + " where project_id=%s" % project_id

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