# coding: utf8
from django.db import connection


def get_search_result(search_key):
    cursor = connection.cursor()

    sql = """SELECT
            m.project_name as "项目名称",
            m.project_number as "项目编码",
            m.status as "项目状态",
            m.create_time as "项目创建时间",
            m.cust_user as "客户",
            s.species as "物种",
            d.sample_name as "样品名称",
            d.sample_id as "样品ID",
            d.sendsample_time as "送样时间",
            d.downmachine_num as "下机时间"
             FROM sample_project_master m
             inner join sample_info_detail d on d.project_id=m.id
             inner join send_sample s on s.project_id=m.id
    """

    sql2 = """select
              ss.project_number,
              ss.sample_name,
              ss.sample_id,
              ss.om_id,
              ss.species,
              qc.results,
              um.data_count,
              dm.data_count
              from send_sample ss
              left join quality_check qc on ss.sample_id=qc.sample_id
              left join upmachine um on qc.sample_id=um.sample_id
              left join downmachine dm on um.sample_id=dm.sample_id
           """
    condition = """
                where (ss.project_number='{key}' or ss.sample_name='{key}' or ss.species='{key}' or qc.sample_id='{key}')
                and ss.status='Y' and (qc.status='Y' or qc.status is NULL)
                and (um.status='Y' or um.status is NULL)
                and (dm.status='Y' or dm.status is NULL)
                """
    sql2 += condition.format(key=search_key)
    cursor.execute(sql2)
    results = cursor.fetchall()

    table_header = ['项目编号', '样品名称', '样品编号', 'OMID', '物种', '判定结果', '上机数据量', '下机数据量']
    table_values = results

    return table_header, table_values
