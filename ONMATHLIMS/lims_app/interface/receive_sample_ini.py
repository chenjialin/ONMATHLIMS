# coding: utf8
from django.db import connection


def get_proj_name_by_id(project_id):
    cmd = "SELECT project_number FROM sample_project_master where id='%s'" % project_id
    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchone()

    return result[0] if result else "请选择项目"


def get_all_proj_info():
    cmd = "select id, project_number from sample_project_master"
    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()

    return result


def get_sample_by_project(project_id):
    """
    :param project_id:
    :return:
    """
    cmd = """select d.id sample_id, d.sample_name, m.project_name, express_number, sendsample_time, sendsample_comment 
              from sample_info_detail d inner join sample_project_master m on m.id=d.project_id
             where project_id='%s' """ % project_id

    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()

    return result
