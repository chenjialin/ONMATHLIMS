# coding: utf8
from django.db import connection


def get_attachment(project_id, attachment_type):
    cmd = """SELECT a.filename,a.upload_time,u.username
     FROM attachment a inner join user_info u on a.upload_user_id=u.id
     where project_id=%s and file_type='%s'""" % (project_id, attachment_type)

    cursor = connection.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()

    return result
