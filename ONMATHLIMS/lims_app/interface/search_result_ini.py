# coding: utf8
from django.db import connection


def get_search_result(search_key):
    search_type = 'sample'
    if 'ONMATH' in search_key:
        search_type = 'project'
    cursor = connection.cursor()
    sql = """SELECT
            m.project_name as "项目名称",
            m.project_number as "项目编码",
            m.status as "项目状态",
            m.create_time as "项目创建时间",
            m.cust_user as "客户",
            d.sample_name as "样品名称",
            d.sendsample_time as "送样时间",
            d.downmachine_num as "下机时间"
             FROM sample_project_master m
             inner join sample_info_detail d on d.project_id=m.id
    """
    condition = " where m.project_number='%s'" if search_type == 'project' else " where d.sample_name='%s'"
    sql += condition % search_key
    cursor.execute(sql)
    results = cursor.fetchall()

    table_header = ['项目名称', '项目编码', '项目状态', '项目创建时间', '客户', '样品名称', '送样时间', '下机时间']
    table_values = results

    return table_header, table_values
