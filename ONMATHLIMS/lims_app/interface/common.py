# coding: utf8
from django.db import connection


def get_attachment(project_id, attachment_type):
    if attachment_type == 'upmachine' or attachment_type == 'downmachine':
        cmd = """SELECT a.id,a.filename,a.upload_time,a.comment,a.location,u.username
        FROM attachment a inner join user_info u on a.upload_user_id=u.id
        where project_id='%s' and file_type='%s'""" % (project_id, attachment_type)
    else:
        cmd = """SELECT a.filename,a.upload_time,u.username
        FROM attachment a inner join user_info u on a.upload_user_id=u.id
        WHERE project_id='%s' and file_type='%s'""" % (project_id, attachment_type)

    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()

    return result


def get_projec_id_by_project_num(project_num):
    cmd = "select id from sample_project_master where project_number='%s' limit 1" % project_num
    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchone()

    return result[0] if result else 0


def get_project_info(project_id):
    cmd = """SELECT action, time, manager FROM SEQ_SA_INFO.project_log_table where
      project_id=%s order by id desc limit 20""" % project_id

    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()

    return result
