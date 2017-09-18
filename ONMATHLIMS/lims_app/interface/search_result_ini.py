# coding: utf8
from django.db import connection


def get_search_result(search_key):
    cursor = connection.cursor()

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
                where (ss.project_number='{key}' or
                ss.sample_name='{key}' or
                ss.species='{key}' or
                qc.sample_id='{key}')
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
